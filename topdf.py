from PyPDF2 import PdfWriter
from PIL import Image
import os
#https://cosmosproject.tistory.com/343


def convert_images_to_pdf(image_paths, output_path, i):
    print(image_paths)
    file_list = os.listdir(image_paths)
    list_imgs=[]

    for file in file_list[1:]:
        list_imgs.append(Image.open(image_paths+"/"+str(file)).convert('RGB'))
    img_main=Image.open(image_paths+"/"+str(file_list[0])).convert('RGB')

    img_main.save(output_path+"/하이큐 {}권.pdf".format(i),save_all=True, append_images=list_imgs)




for i in range(31,46,1):
    # Path to the directory containing the images
    images_directory = 'C:/Users/lovek/Desktop/wedisk/hi/'+str(i)+'/merged'

    # Output PDF file path
    output_pdf_path = 'C:/Users/lovek/Desktop/wedisk/final_output'

    # Get the list of image files in the directory
    image_files = [os.path.join(images_directory, filename) for filename in os.listdir(images_directory)
                if filename.endswith('.jpg')]

    # Convert the images to a PDF file
    convert_images_to_pdf(images_directory, output_pdf_path, i)
