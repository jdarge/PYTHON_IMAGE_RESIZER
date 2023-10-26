from PIL import Image
import os

def expand2square(pil_img, background_color):
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result

source_dir = "source_images"
output_dir = "squared_images"
fill_color = (0, 0, 0) # RGB Black

dir = os.listdir()
print(dir)
dir = os.listdir(source_dir)
print(dir)

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

for subdir in dir:

    if '.py' in subdir:
        continue

    if not os.path.exists(source_dir + '/' + subdir):
        os.mkdir(source_dir + '/' + subdir)

    if not os.path.exists(output_dir + '/' + subdir):
        os.mkdir(output_dir + '/' + subdir)

    images = [i for i in os.listdir(source_dir + '/' + subdir) if '.jpg' in i]
    print(images)

    for img in images:
        old = Image.open(source_dir + '/' + subdir + '/' + img)
        new = expand2square(old, fill_color)
        new.save(output_dir + '/' + subdir + '/' + img)

