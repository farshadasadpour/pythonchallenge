from PIL import Image

im = Image.open('./files/cave.jpg')
weight,height = im.size

even = Image.new('RGB',(weight//2,height//2))
odd = Image.new("RGB",(weight//2,height//2))

for i in range(weight):
    for j in range(height):
        p = im.getpixel((i,j))
        if (i+j)%2 == 1:
            odd.putpixel((i//2,j//2),p)
        else:
            even.putpixel((i//2,j//2),p)

even.save('./files/even.jpg')
odd.save('./files/odd.jpg')


# answer is evil