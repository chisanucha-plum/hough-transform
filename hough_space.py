import cv2
import numpy as np


def hough_space(edge):
    h, w = edge.shape
    d = int(np.sqrt(h**2 + w**2))
    acc = np.zeros((2 * d, 180), dtype=np.uint64)

    y, x = np.nonzero(edge)
    for xi, yi in zip(x, y):
        for t in range(180):
            rho = int(xi * np.cos(np.radians(t)) + yi * np.sin(np.radians(t)))
            acc[rho + d, t] += 1

    top10_idx = np.argsort(acc.flatten())[-10:][::-1]

    for i, idx in enumerate(top10_idx, 1):
        rho_idx, theta_idx = idx // 180, idx % 180
        print(
            f"{i}. ρ={rho_idx - d:4d}, θ={theta_idx:3d}°, votes={acc[rho_idx, theta_idx]}"
        )

    hough_img = (np.log(acc + 1) / np.log(acc + 1).max() * 255).astype(np.uint8)
    hough_spaces = cv2.applyColorMap(hough_img, cv2.COLORMAP_HOT)

    for idx in top10_idx:
        pos = (idx % 180, idx // 180)
        cv2.circle(hough_spaces, pos, 5, (0, 255, 0), -1)
        cv2.circle(hough_spaces, pos, 6, (255, 255, 255), 2)

    return hough_spaces
