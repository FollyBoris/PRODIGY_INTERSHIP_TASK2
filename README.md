# PRODIGY_INTERSHIP_TASK2
 
# Image Encryption and Decryption Tool

This project provides a simple tool for encrypting and decrypting images using a key-based XOR operation. The tool can be run from the command line and supports various image formats such as `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, and `.webp`.

## Features

- Encrypt images with a specified key
- Decrypt images with the same key used for encryption
- Supports a wide range of image formats
- Command-line interface for easy usage

## Requirements

- Python 3.x
- NumPy
- Pillow (PIL)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/FollyBoris/PRODIGY_INTERSHIP_TASK2.git
   cd PRODIGY_INTERSHIP_TASK2
   ```
**##Install the required libraries:**

```bash
pip install numpy pillow
```

**##Usage **
The tool can be used directly from the command line or interactively through user prompts.

**###Command Line Usage**
Encrypt an image:

```bash

python main.py --mode encrypt --path path_to_image.jpg --name encrypted_image --key 123

```
**###Decrypt an image:**
```bash

python main.py --mode decrypt --path path_to_encrypted_image.jpg --name decrypted_image --key 123
```

**###Interactive Usage**
Run the script without arguments to use the interactive mode:

```
bash
python main.py
```

You will be prompted to choose between encryption and decryption, provide the image path, save name, and key.
