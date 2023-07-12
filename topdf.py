from PyPDF2 import PdfWriter
from PIL import Image
import os
#https://cosmosproject.tistory.com/343


def convert_images_to_pdf(image_paths, output_path, chapter):
    print(image_paths)
    file_list = os.listdir(image_paths)
    list_imgs=[]

    for i in range(2, len(file_list)+1, 1):
        # print(image_paths+"/"+str(i)+".jpg")
        list_imgs.append(Image.open(image_paths+"/"+str(i)+".jpg").convert('RGB'))
    img_main=Image.open(image_paths+"/1.jpg").convert('RGB')

    img_main.save(output_path+"/Fullmetal Alchemist {}.pdf".format(chapter),save_all=True, append_images=list_imgs)
    




for i in range(1,7,1):
    # Path to the directory containing the images
    images_directory = 'C:/Users/user/Downloads/FA/'+str(i)+'/merged'

    # Output PDF file path
    output_pdf_path = 'C:/Users/user/Downloads/FA'

    # Get the list of image files in the directory
    image_files = [os.path.join(images_directory, filename) for filename in os.listdir(images_directory)
                if filename.endswith('.jpg')]

    # Convert the images to a PDF file
    convert_images_to_pdf(images_directory, output_pdf_path, i)
