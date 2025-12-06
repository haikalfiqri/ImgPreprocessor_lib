# imagepreproc_haikalfiqri/preprocessing.py

import cv2
import numpy as np
from PIL import Image


# ---------- Color conversion ----------
#convert color conversion of an image

# ---------- Noise reduction ----------
#convert a noisy image to a denoised image

def denoise_gaussian(image: np.ndarray,
                     ksize: int = 11) -> np.ndarray:
    return cv2.GaussianBlur(image, (ksize, ksize), 0)


def denoise_median(image: np.ndarray,
                   ksize: int = 11) -> np.ndarray:
    return cv2.medianBlur(image, ksize)

def denoise_bilateral(image: np.ndarray,
                      d: int = 15,
                      sigma_color: int = 100,
                      sigma_space: int = 100) -> np.ndarray:
    return cv2.bilateralFilter(image, d, sigma_color, sigma_space)

# ---------- Resizing ----------
#convert an image to a resized image
