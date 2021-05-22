import requests
from bs4 import BeautifulSoup
import urllib
import os


load_url = "https://www.security-next.com/"
html = requests.get(load_url)
soup = BeautifulSoup(html.content,"html.parser")

head = soup.find(class_="content")
for element in head.find_all("a"):
    print(element.text)


filename = "news/linklist.txt"
with open(filename,"w")as f:
    for element in head.find_all("a"):
        url = element.get("href")
        link_url = urllib.parse.urljoin(load_url,url)
        f.write(element.text+"\n")
        f.write(link_url+"\n")
        f.write("\n")
