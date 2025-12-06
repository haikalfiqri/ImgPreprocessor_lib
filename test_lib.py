import unittest
import numpy as np
from PIL import Image
from imageModule import (
    convert_color,
    denoise_gaussian,
    denoise_median,
    denoise_bilateral,
    resize_opencv,
    resize_pillow
)


class TestConvertColor(unittest.TestCase):
    
    def test_convert_to_rgb(self):
        """Test BGR to RGB conversion."""
        # Create a BGR image with blue channel = 255
        bgr_image = np.zeros((50, 50, 3), dtype=np.uint8)
        bgr_image[:, :, 0] = 255  # Blue in BGR
        
        rgb_image = convert_color(bgr_image, mode="rgb")
        
        # In RGB, blue should be in channel 2
        self.assertEqual(rgb_image[0, 0, 2], 255)
        self.assertEqual(rgb_image[0, 0, 0], 0)
    
    def test_convert_to_gray(self):
        """Test BGR to grayscale conversion."""
        bgr_image = np.ones((50, 50, 3), dtype=np.uint8) * 128
        
        gray_image = convert_color(bgr_image, mode="gray")
        
        # Grayscale should be 2D
        self.assertEqual(len(gray_image.shape), 2)
        self.assertEqual(gray_image.shape, (50, 50))
    
    def test_convert_to_hsv(self):
        """Test BGR to HSV conversion."""
        bgr_image = np.ones((50, 50, 3), dtype=np.uint8) * 100
        
        hsv_image = convert_color(bgr_image, mode="hsv")
        
        # HSV should have 3 channels
        self.assertEqual(hsv_image.shape, (50, 50, 3))
    
    def test_convert_to_lab(self):
        """Test BGR to LAB conversion."""
        bgr_image = np.ones((50, 50, 3), dtype=np.uint8) * 150
        
        lab_image = convert_color(bgr_image, mode="lab")
        
        # LAB should have 3 channels
        self.assertEqual(lab_image.shape, (50, 50, 3))



class TestDenoiseGaussian(unittest.TestCase):
    
    def test_gaussian_blur_returns_same_shape(self):
        """Test that Gaussian blur maintains image dimensions."""
        test_image = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
        
        blurred = denoise_gaussian(test_image, ksize=5)
        
        self.assertEqual(blurred.shape, test_image.shape)


class TestDenoiseMedian(unittest.TestCase):
    
    def test_median_blur_returns_same_shape(self):
        """Test that median blur maintains image dimensions."""
        test_image = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
        
        blurred = denoise_median(test_image, ksize=5)
        
        self.assertEqual(blurred.shape, test_image.shape)

class TestDenoiseBilateral(unittest.TestCase):
    
    def test_bilateral_filter_returns_same_shape(self):
        """Test that bilateral filter maintains image dimensions."""
        test_image = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
        
        filtered = denoise_bilateral(test_image, d=9, sigma_color=75, sigma_space=75)
        
        self.assertEqual(filtered.shape, test_image.shape)
    


class TestResizeOpenCV(unittest.TestCase):
    
    def test_resize_to_specific_dimensions(self):
        """Test that OpenCV resize produces exact dimensions."""
        test_image = np.ones((200, 300, 3), dtype=np.uint8)
        
        resized = resize_opencv(test_image, width=100, height=50)
        
        self.assertEqual(resized.shape, (50, 100, 3))


class TestResizePillow(unittest.TestCase):
    
    def test_pillow_resize_to_specific_dimensions(self):
        """Test that Pillow resize produces exact dimensions."""
        pil_image = Image.new('RGB', (300, 200), color='red')
        
        resized = resize_pillow(pil_image, width=100, height=50)
        
        self.assertEqual(resized.size, (100, 50))

    

if __name__ == '__main__':
    unittest.main()