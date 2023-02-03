# Place in direc with image folders
# image folders should contain images with the following format: image_1.jpg
# this will create square images with transparent backgrounds

import os 
import time
from PIL import Image

count_current = 1
count_total = 0

try: 
    folders = os.listdir(".")
except Exception as e:
    print(e)
count_total = len(folders)
for folder in folders:
    try: 
        images = os.listdir(folder+"/")
    except Exception as e: 
        continue

    print(f'[{count_current}/{count_total}] | {folder}')

    for image in images:

        file_name = folder+'/'+image
        command = "rembg i" +' '+ folder+'/'+image +' '+ folder+'/_'+image

        if file_name.split('.')[1] == 'png':
            continue

        try :
            # run background remover
            os.system(command)

            # remove original file and then rename new file to old name
            os.remove(file_name)
            os.rename(folder+'/_'+image, file_name)

            # create the file name with .png extension
            no_ext = file_name.split('.')[0]
            file_name_png = no_ext+'.png'

            # delete nonsense and save goodness
            im = Image.open(file_name)
            im2 = im.crop(im.getbbox())
            im2.save(file_name_png)
            os.remove(file_name)

            # make the image square
            im = Image.open(file_name_png)
            x,y = im.size
            size = max(512, x, y)
            new_im = Image.new('RGBA', (size,size), (0,0,0,0))
            new_im.paste(im, (int ((size-x) /2), int((size-y) / 2)))
            new_im.save(file_name_png)
       
        except Exception as e:
            print (e)

    count_current=count_current+1


print('DONE')
