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

def resize_for_display(image: np.ndarray,
                       max_width: int = 800,
                       max_height: int = 600) -> np.ndarray:
    """Resize image to fit in a box while keeping aspect ratio."""
    h, w = image.shape[:2]
    scale = min(max_width / w, max_height / h, 1.0)
    new_size = (int(w * scale), int(h * scale))


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
def resize_opencv(image: np.ndarray,
                  width: int,
                  height: int) -> np.ndarray:
    return cv2.resize(image, (width, height))

def resize_pillow(pil_image: Image.Image,
                  width: int,
                  height: int) -> Image.Image:
    return pil_image.resize((width, height))
