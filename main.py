#!pip install numpy pillow
from cryptage import image_encrypt, image_decrypt
from cryptage import crypt_algo
import argparse
from PIL import Image
import numpy as np

def main():
    # take the argument directly if the user launch python main.py --mode encrypt --message "Hello!" --shift 2
    parser = argparse.ArgumentParser(description="Image Encryption/Decryption Tool")
    parser.add_argument("--mode", choices=["encrypt", "decrypt"], help="Mode of operation")
    parser.add_argument("--path", help="Image path")
    parser.add_argument("--name", help="The exit file name")
    parser.add_argument("--key", type=int, help="Key value for the decryption")
    args = parser.parse_args()
    
    if not args.mode and not args.path and not args.name and not args.key:
        # take the user choice, encrypt or decrypt
        choice = int(input(" Do you want to encrypt or decrypt the image \n 1     Encryption \n 2     Decryption \n"))
        
        # verify the user option is correct
        if choice == 1 or choice == 2:
            
            print("Image must be in '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'")
            # take the image path and the encryption name / decryption name
            
            img_path = str(input("\n Enter the image path:\n"))
            save_name = str(input("\n Enter the image save name:\n"))
            key = str(input("\n Enter the key:\n"))
            
            # start process //encryption or //decryption
            if choice == 1:
                print(image_encrypt(img_path, save_name, key))
            else :
                
                print(image_decrypt(img_path, save_name, key))
    
    elif args.mode=="encrypt":
        if not args.path:
            print("Error: --path argument is required")
        if not args.name:
            print("Error: --name argument is required")
        else:
            print(image_encrypt(args.path,args.name))
    elif args.mode=="decrypt":
        if not args.path:
            print("Error: --path argument is required")
        if not args.name:
            print("Error: --name argument is required")
        if not args.key:
            print("Error: --key argument is required")
        else:
            print(image_decrypt(args.path,args.name, args.key))

if __name__ =="__main__":
    main()