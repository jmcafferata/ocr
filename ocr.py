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
    parser = argparse.ArgumentParser(description="OCR all PNG files in a directory")
    parser.add_argument('directory', help="Directory to scan for png files")
    parser.add_argument('output_file', help="File to output the OCR'd text")
    parser.add_argument('--lang', default='spa', help="Language for Tesseract OCR")
    parser.add_argument('--rotation', type=float, default=0, help="Rotation angle for the images")

    args = parser.parse_args()

    ocr_directory(args.directory, args.output_file, args.lang, args.rotation)
