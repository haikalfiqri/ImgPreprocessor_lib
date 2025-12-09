# Image Preprocessing Toolkit  
### Final Project — CLI Application + Python Processing Library  
### Created by: Haikal Fiqri, Zarith Imran , Akif Najwan , Acap Padil

## Overview

The **Image Preprocessing Toolkit** is a two-part project consisting of:

### **(1) Python Library — `imgpreprocessor-lib`**
A reusable Python package containing all core image preprocessing functions such as:
- Color space conversion  
- Noise reduction  
- Image resizing (OpenCV & Pillow)  
- Display-safe auto resizing  

 GitHub Repository:  
https://github.com/haikalfiqri/ImgPreprocessor_lib  

TestPyPI Package:  
https://test.pypi.org/project/imgpreprocessor-lib/

### **(2)CLI Application — `ImgPreprocessor_mainCLI`**
A Command-Line Interface (CLI) tool that provides a user-friendly menu that uses the library internally.  
This allows users to perform preprocessing tasks **without writing code**.

 GitHub Repository (CLI):  
https://github.com/haikalfiqri/ImgPreprocessor_mainCLI

## Project Purpose

This project was developed as a **final  assignment** to demonstrate:

- Packaging Python projects into reusable libraries  
- Publishing packages to TestPyPI  
- Building a functional CLI tool  
- Applying image processing knowledge  
- Integrating multiple modules into one application  
- To demonstrate open source skills such as branching , push , testing and merging

The library is designed to be clean, modular, and easy to integrate into larger machine learning or computer vision workflows, while the CLI provides a hands-on interactive experience.

# Installation Guide (Library + CLI)

The CLI application **requires** the library to be installed first.  
Below are multiple installation options depending on the user’s environment.


## Option 1 — Install the Library from TestPyPI (Recommended)

cmd/bash :
pip install -i https://test.pypi.org/simple/ imgpreprocessor-lib

This installs the latest published version of **imagepreproc_haikalfiqri** which contains:

* `preprocessing.py`
* Internal color, noise, and resizing functions


## Option 2 — Install Library Directly from GitHub (Development Version)

cmd/bash :
pip install git+https://github.com/haikalfiqri/ImgPreprocessor_lib.git


Useful for:

* Testing latest updates
* Working on development branches


#  Installing and Running the CLI Application

Clone the CLI repository:

cmd/bash
git clone https://github.com/haikalfiqri/ImgPreprocessor_mainCLI.git
cd ImgPreprocessor_mainCLI

Run the main program:

cmd/bash
python mainPreprocessor.py

If you see this banner, everything is working well at this point:

**WELCOME TO IMAGE PREPROCESSING TOOLKIT**


# Features (Detailed)

The project is split into two main components: **library functions** and **CLI modules**.

##  1. Color Space Conversion

Available modes:

* `rgb` – Convert BGR → RGB
* `gray` – Convert BGR → Grayscale
* `hsv` – Convert BGR → HSV
* `lab` – Convert BGR → CIELAB

Relevant function:

python :
preprocessing.convert_color(image, mode="rgb")

Examples:

* RGB for display
* Grayscale for filtering
* HSV for color-based segmentation
* LAB for luminance/contrast processing


## 🔹 2. Noise Reduction

### Supported Filters:

| Filter               | Function              | Use Case                              |
| -------------------- | --------------------- | ------------------------------------- |
| **Gaussian Blur**    | `denoise_gaussian()`  | Smooths image, reduces Gaussian noise |
| **Median Blur**      | `denoise_median()`    | Removes salt-and-pepper noise         |
| **Bilateral Filter** | `denoise_bilateral()` | Smooths while keeping edges           |

Example:

python :
preprocessing.denoise_bilateral(img, d=15, sigma_color=100, sigma_space=100)


##  3. Image Resizing

Two independent resizing engines:

### OpenCV Backend

python :
preprocessing.resize_opencv(image, width, height)

###  Pillow Backend

python :
preprocessing.resize_pillow(pil_image, width, height)

###  Auto Resizing (Safe for Display)

Ensures large images fit comfortably on screen:

python :
preprocessing.resize_for_display(image)


#  CLI Application Flow (Detailed)

When the user runs:

cmd/bash :
python mainPreprocessor.py

They will get a menu as follows:

1. Color Space Conversion
2. Noise Reduction
3. Image Resizing
4. Exit

Each option opens a sub-menu:

## 1. Color Space Module

Steps:

1. User inputs image path
2. User selects target color space
3. Program converts using the library
4. Output displayed using OpenCV’s `imshow()`


## 2. Noise Reduction Module

User chooses one of the option provided:

* Gaussian
* Median
* Bilateral

Inputs:

* Kernel size
* Optional sigma values


##  3. Image Resizing Module

User selects backend:

* OpenCV
* Pillow (PIL)

Then inputs:

* Width
* Height

Program displays the resized image.




# Example Code (For Developers)

python :
import cv2
from imagepreproc_haikalfiqri import preprocessing

# load image
img = cv2.imread("sample.jpg")

# convert to grayscale
gray = preprocessing.convert_color(img, mode="gray")

# apply gaussian noise reduction
filtered = preprocessing.denoise_gaussian(gray, ksize=11)

# resize image
resized = preprocessing.resize_opencv(filtered, width=500, height=500)

# show result
cv2.imshow("Output", resized)
cv2.waitKey(0)
```



# Requirements for runnning this program

### System Requirements

* Python 3.8+
* OpenCV (`cv2`)
* Pillow (`PIL`)
* NumPy

Install manually if missing:

cmd/bash
pip install opencv-python pillow numpy


#  Project Authors

This project was created by:

* **Haikal Fiqri**
* **Zarith Imran**
* **Akif Najwan**
* **Acap Padil**




Library:
[https://github.com/haikalfiqri/ImgPreprocessor_lib](https://github.com/haikalfiqri/ImgPreprocessor_lib)

CLI Tool:
[https://github.com/haikalfiqri/ImgPreprocessor_mainCLI](https://github.com/haikalfiqri/ImgPreprocessor_mainCLI)

