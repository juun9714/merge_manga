from PIL import Image
import os



def merge_images(directory):
    # Get the list of files in the directory
    file_list = os.listdir(directory)
    sorted_files = sorted(file_list)
    count=1
    for i in range(1, len(sorted_files)+1, 2):

        try:
            image1=Image.open(directory+'/'+str(i)+".jpg")
            try:
                image2=Image.open(directory+'/'+str(i+1)+".jpg")
            except:
                image1.save(directory+'/'+"merged/{}.jpg".format(count),"JPEG")
                return

            image1size=image1.size
            image2size=image2.size

            newImage=Image.new('RGB',(2*image1size[0], image1size[1]), (250,250,250))
            newImage.paste(image2,(0,0))
            newImage.paste(image1,(image2size[0],0))
            newImage.save(directory+'/'+"merged/{}.jpg".format(count),"JPEG")
            count+=1
        except:
            return


for i in range(24,25,1):
    directory_path = '/Users/june/Desktop/manga/merge_manga/hi_fin/'+str(i)
    # Call the function to rename files
    print(directory_path)
    merge_images(directory_path)

