#!pip install pillow pycryptodome

from PIL import Image
import numpy as np
import os


def image_pixel_bytes(image_path):
    # Open the image and convert it to RGB format
    image = Image.open(image_path).convert('RGB')
    # use np.array to convert in matrix
    pixels = np.array(image)
    # extension of the image
    ext = check_image_extension(image_path)
    
    
    return pixels, ext
    
def check_image_extension(file_path):
    # Split the file path into root and extension
    root, ext = os.path.splitext(file_path)
    
    # List of common image extensions
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}
    
    # Check if the file extension is an image extension
    if ext.lower() in image_extensions:
        return ext.lower()
    else:
        print("Is not image path")