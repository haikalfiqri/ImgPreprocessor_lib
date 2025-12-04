# imagepreproc_haikalfiqri/preprocessing.py

import cv2
import numpy as np
from PIL import Image


# ---------- Color conversion ----------
#convert color conversion of an image

# ---------- Noise reduction ----------
#convert a noisy image to a denoised image

# ---------- Resizing ----------
#convert an image to a resized image
def resize_opencv(image: np.ndarray,
                  width: int,
                  height: int) -> np.ndarray:
    return cv2.resize(image, (width, height))
