from bz2 import decompress

un= b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw= b"BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08"


print(f"user is:{decompress(un).decode('utf-8')}")
print(f"pass is:{decompress(pw).decode('utf-8')}")


"""
user is:huge
pass is:file
"""