import requests
import re
link = input("Input link\n")
html = requests.get(link)
links = re.findall("(href=\"https://[^>]*)", html.text)
for i in links:
    a = re.findall("(https:\/\/[^\"]*)", i)
    print("link =", a)


