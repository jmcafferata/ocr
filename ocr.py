import os
import argparse
from PIL import Image
import pytesseract

def ocr_directory(directory, output_file, language, rotation):
    with open(output_file, 'w', encoding='utf-8') as f:
        for filename in os.listdir(directory):
            if filename.endswith('.png'):
                with Image.open(os.path.join(directory, filename)) as img:
                    img = img.rotate(rotation)
                    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
                    text = pytesseract.image_to_string(img, lang=language)
                    f.write(text + '\n')

if __name__ == "__main__":

    directory = 'output'
    output_file = 'output.txt'
    language = 'spa'
    rotation = 0

    ocr_directory(directory, output_file, language, rotation)
