import zipfile
import re


# url="https://www.pythonchallenge.com/pc/def/channel.zip"


archive = zipfile.ZipFile('/home/master/Downloads/channel.zip', 'r')
next_number = re.findall(r"([0-9]+)",archive.read("90052.txt").decode())
next_number="".join(next_number)+".txt"

comment_list = list()

for item in range(len(archive.namelist())):
    # print(archive.read(next_number).decode())
    comment_list.append(archive.getinfo(next_number).comment.decode())
    next_number = re.findall(r"([0-9]+)",archive.read(next_number).decode())
    if len(next_number) > 0:
        next_number="".join(next_number)+".txt"
        last_num = next_number
    else:
        print(archive.read(last_num).decode())
        break
print(last_num)
print("".join(comment_list))


"""
***************************************************************
****************************************************************
**                                                            **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
**   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
**   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
**                                                            **
****************************************************************
 **************************************************************
"""