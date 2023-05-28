import os
import argparse
from pdf2image import convert_from_path

def pdf_to_png():
    # get the files that start with pdf
    pdf_file = [f for f in os.listdir('.') if f.endswith('.pdf')][0]
    

    # output folder is output
    output_folder = 'output'
    os.makedirs(output_folder, exist_ok=True)
    
    # Convert PDF to a list of PIL Image objects
    images = convert_from_path(pdf_file)
    
    for i, image in enumerate(images):
        print(f'Converting page {i}')
        image.save(os.path.join(output_folder, f'output_{i}.png'), 'PNG')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a PDF to PNG images")

    args = parser.parse_args()

    pdf_to_png()
