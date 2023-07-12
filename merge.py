from PIL import Image
import os



def merge_images(directory):
    # Get the list of files in the directory
    file_list = os.listdir(directory)
    sorted_files = sorted(file_list)
    sorted_files.pop(-1)
    #print(sorted_files)
    count=1
    for i in range(1, len(sorted_files)+1, 2):
        try:
            image1=Image.open(directory+'/'+str(i)+".jpg")
            image1size=image1.size
            if image1size[0]==1800: # image 1이 큰 사진
                image1.save(directory+'/'+"merged/{}.jpg".format(count),"JPEG")
                count+=1
                continue
            else:
                try:
                    image2=Image.open(directory+'/'+str(i+1)+".jpg")
                    image2size=image2.size
                    
                    if image2size[0]==1800: # image1은 작은 사진, image 2가 큰 사진 -> image1도 저장하고, image2도 저장해줘야 함
                        newImage=Image.new('RGB',(2*image1size[0], image1size[1]), (250,250,250))
                        newImage.paste(image1,(image1size[0],0))
                        newImage.save(directory+'/'+"merged/{}.jpg".format(count),"JPEG")
                        count+=1
                        image2.save(directory+'/'+"merged/{}.jpg".format(count),"JPEG")
                        count+=1
                        continue
                    else: # image 1, 2 모두 작은 사이즈 
                        newImage=Image.new('RGB',(2*image1size[0], image1size[1]), (250,250,250))
                        newImage.paste(image2,(0,0))
                        newImage.paste(image1,(image2size[0],0))
                        newImage.save(directory+'/'+"merged/{}.jpg".format(count),"JPEG")
                        count+=1
                except:
                    # image1이 마지막 장
                    image1.save(directory+'/'+"merged/{}.jpg".format(count),"JPEG")
                    return

            
        except:
            return
    


for i in range(2,28,1):
    directory_path = 'C:/Users/user/Downloads/FA/'+str(i)
    # Call the function to rename files
    print(directory_path)
    merge_images(directory_path)

