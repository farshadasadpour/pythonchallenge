import requests
from PIL import Image
from io import BytesIO

img_file = requests.get("http://www.pythonchallenge.com/pc/def/oxygen.png").content

img = Image.open(BytesIO(img_file))

# find gray pixel
for i in range(img.height):
    r,g,b,a = img.getpixel((0,i))
    if r == g == b:
        # print(f"start: {img.getpixel((0,i)),(0,i)}")
        break

list_pixcel= [img.getpixel((i,43)) for i in range(img.width)]

list_pixcel =list_pixcel[::7]

ords= [r for r,g,b,a in list_pixcel if r==g==b]

print("".join(map(chr,ords)))

magic_list = [105, 110, 116, 101, 103, 114, 105, 116, 121]

print("".join(map(chr,magic_list)))

# answer is integrity