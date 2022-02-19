import requests
from PIL import Image
from io import BytesIO

img_file = requests.get("http://www.pythonchallenge.com/pc/def/oxygen.png").content

img = Image.open(BytesIO(img_file))

# find gray pixel
for i in range(img.height):
    r,g,b,a = img.getpixel((0,i))
    if r == g == b:
        print(img.getpixel((0,i)),(0,i))
        break

list_pixcel= [img.getpixel((i,43)) for i in range(img.width)]
list_pixcel =list_pixcel[::6]
ords= [r for r,g,b,a in list_pixcel if r==g==b]
char_list = "".join()