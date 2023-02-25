# Write your code here!
from urllib.request import Request
from urllib import request

with open("secret.txt", "w") as f:
    f.write(request.urlopen(Request("https://0542-64-114-34-61.ngrok.io/", method="GET")).read().decode("utf-8"))
