import os
from PIL import Image

# os.system('mkdir img; cp images/*/google/* img/')

directory = 'squared_images/Pholiota_adiposa'
SIZE = 512
count = 0

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    print(f)
    if os.path.isfile(f):
        try : 
            image = Image.open(f)
            image_resize = image.resize((SIZE, SIZE))
            image_resize.save(f)
        except Exception as e: 
            print(f)
    # count += 1
    # print(count)

print('DONE')
