from urllib.request import urlopen
import pickle

base_url = "http://www.pythonchallenge.com/pc/def/banner.p"
data_from_web = urlopen(base_url)
data = pickle.load(data_from_web)
for line in data:
    print("".join([k * v for k, v in line]))

# answer is channel
