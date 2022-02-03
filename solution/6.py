import zipfile
import re


# url="https://www.pythonchallenge.com/pc/def/channel.zip"


archive = zipfile.ZipFile('/home/master/Downloads/channel.zip', 'r')
next_number = re.findall(r"([0-9]+)",str(archive.read("90052.txt")))
next_number="".join(next_number)+".txt"

for item in range(len(archive.namelist())):
    next_number = re.findall(r"([0-9]+)",str(archive.read(next_number)))
    if len(next_number) > 0:
        next_number="".join(next_number)+".txt"
        last_num = next_number
    else:
        print(str(archive.read(last_num)))
        break
