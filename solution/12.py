# http://www.pythonchallenge.com/pc/return/evil1.jpg
# http://www.pythonchallenge.com/pc/return/evil2.jpg
# http://www.pythonchallenge.com/pc/return/evil3.jpg
# http://www.pythonchallenge.com/pc/return/evil4.jpg
# curl -u huge:file http://www.pythonchallenge.com/pc/return/evil4.jpg

info = open("./files/evil2.gfx", 'rb').read()
for i in range(5):
    open('./files/%d.jpg' % i, 'wb').write(info[i::5])

# answer is disproportional
