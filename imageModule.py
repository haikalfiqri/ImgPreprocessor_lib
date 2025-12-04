# imagepreproc_haikalfiqri/preprocessing.py

import cv2
import numpy as np
from PIL import Image


# ---------- Color conversion ----------
def convert_color(image: np.ndarray, mode: str = "rgb") -> np.ndarray:
    """Convert BGR OpenCV image to another color space."""
    mode = mode.lower()
    if mode == "rgb":
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    if mode == "gray":
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if mode == "hsv":
        return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    if mode == "lab":
        return cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    raise ValueError(f"Unsupported mode: {mode}")


# ---------- Noise reduction ----------
#convert a noisy image to a denoised image

# ---------- Resizing ----------
#convert an image to a resized image
