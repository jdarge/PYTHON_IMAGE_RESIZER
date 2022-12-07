import os
from PIL import Image

# os.system('mkdir img; cp images/*/google/* img/')

directory = 'img'
size = 64
count = 0

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        image = Image.open(f)
        image_resize = image.resize((SIZE,SIZE))
        image_resize.save(f)
    count += 1
    print(count)

print('DONE')
