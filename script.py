import requests

print(requests.__version__)
print(requests.get("http://www.google.com/").status_code)

out = requests.get("https://raw.githubusercontent.com/arthuruwalaka/404-lab1/main/script.py")
print(out.text)
