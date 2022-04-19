import urllib3
import re


class Service:
    def __init__(self, url):
        self.http = urllib3.PoolManager()
        self.url = url
        self.method = 'GET'

    def _status_request(self):
        r = self.http.request(self.method, self.url)
        return r.status

    def _data_request(self, url):
        r = self.http.request(self.method, url)
        return str(r.data)

    def _get_number(self, url):
        f = re.findall("([0-9]+)", self._data_request(url))
        print(self._data_request(url))
        return "".join(f)


base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

s = Service(base_url)
num = "12345"
while True:
    num = s._get_number(base_url + num)
    if num == None or num == "":
        break
    # num = str(int(num)//2)
    # num = s._get_number(base_url+num)

    # answer is 'peak.html'
