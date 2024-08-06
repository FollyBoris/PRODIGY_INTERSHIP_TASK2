import numpy as np
from PIL import Image
from image_pixel_byte import image_pixel_bytes

def crypt_algo(image_path, key, mode = "encrypt"):
    #  mode = "encrypt"
    image_pixel, ext= image_pixel_bytes(image_path)
    #determine the pixel size (shape)
    rows, cols, rgb = image_pixel.shape
    
    #create a matrix using a key value
    key_matrix = np.full((rows, cols, rgb), fill_value=key, dtype=np.uint8)
    
    if mode == "decrypt":
        key_matrix = -key_matrix
        
    # matrix = image_path + key_matrix
    matrix = np.add(image_pixel, key_matrix)
    # Verify if the value is between 0, 255
    matrix = np.clip(matrix, 0, 255)
    
    #convert the matrix in image
    image = Image.fromarray(matrix.astype(np.uint8))
    return image, ext
    
    
def image_encrypt(image_path, save_image_name, key):
    #save the image in the current directory
    image, ext = crypt_algo(image_path, key)
    image_name = save_image_name + ext
    image.save(image_name)
  
    return f'Encryption complete. Saved as {image_name} in the current directory.'
    
    
def image_decrypt(image_path, save_image_name, key):
    
    #save the image in the current directory
    image, ext = crypt_algo(image_path, key, mode="decrypt")
    image_name = save_image_name + ext
    image.save(image_name)
    
    return f'Decryption complete. Saved as {image_name} in the current directory.'
   
