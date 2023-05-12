from PIL import Image
import os



def merge_images(directory):
    # Get the list of files in the directory
    file_list = os.listdir(directory)
    count=1
    for i in range(1, len(file_list), 2):
        image1=Image.open(directory+'/'+str(i)+".jpg")
        try:
            image2=Image.open(directory+'/'+str(i+1)+".jpg")
        except:
            image2.save(directory+'/'+"merged/merge{}.jpg".format(count),"JPEG")
            return

        image1size=image1.size
        image2size=image2.size

        newImage=Image.new('RGB',(2*image1size[0], image1size[1]), (250,250,250))
        newImage.paste(image2,(0,0))
        newImage.paste(image1,(image2size[0],0))
        newImage.save(directory+'/'+"merged/merge{}.jpg".format(count),"JPEG")
        count+=1


for i in range(32,46,1):
    directory_path = 'C:/Users/lovek/Desktop/wedisk/hi/'+str(i)
    # Call the function to rename files
    print(directory_path)
    merge_images(directory_path)