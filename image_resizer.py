# assumes images are grouped into appropriate folders already and is in the root directory alongside the image folders
# i.e TYPEA/TYPEA_1.png

import os 
from PIL import Image 

size = 1024
folders = os.listdir('.')

for folder in folders:
    print(f'FOLDER: {folder}')
    try:
        images = os.listdir(folder+'/')
    except Exception as e: 
        continue
    for image in images: 
        print(f'\t{image}')
        file = folder+'/'+image
        if os.path.isfile(file): 
            try: 
                f = Image.open(file)
                f = f.resize((size,size)) 
                f.save(file)
            except Exception as e: 
                print(f'\n{e}\n')
