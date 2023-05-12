from PyPDF2 import PdfWriter
from PIL import Image
import os
#https://cosmosproject.tistory.com/343


def convert_images_to_pdf(image_paths, output_path):
    pdf_writer = PdfWriter()

    for image_path in image_paths:
        image = Image.open(image_path).convert('RGB')
        width, height = image.size
        pdf_page = pdf_writer.add_blank_page(width=width, height=height)
        pdf_image = pdf_page.add_image(image)
        pdf_writer.add_image(pdf_image)

    with open(output_path, 'wb') as output_file:
        pdf_writer.write(output_file)

# Path to the directory containing the images
images_directory = 'C:/Users/lovek/Desktop/wedisk/hi/1/merged'

# Output PDF file path
output_pdf_path = images_directory

# Get the list of image files in the directory
image_files = [os.path.join(images_directory, filename) for filename in os.listdir(images_directory)
               if filename.endswith('.jpg')]

# Convert the images to a PDF file
convert_images_to_pdf(image_files, output_pdf_path)
