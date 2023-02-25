# Write your code here!

from urllib.request import Request
from urllib import request
from urllib.parse import urlencode

url = "https://0542-64-114-34-61.ngrok.io/"
data = urlencode({ "name": "Amrit" })
data = data.encode("ascii")
req = Request(url, data=data)
response = request.urlopen(req)
print(response.read())

