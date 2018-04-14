from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://ko.wikipedia.org/wiki/%EC%8B%A0%EC%82%AC%EB%8F%99_(%EA%B0%95%EB%82%A8%EA%B5%AC)")
bsObj = BeautifulSoup(html.read(), "html.parser")

elementLinks = bsObj.find("div", {"id":"bodyContent"}).findAll("a",
                       href=re.compile("^(/wiki/)((?!:).)*$"))
print(len(elementLinks))

for link in elementLinks:
    if 'href' in link.attrs:
        print(link.attrs['href'])
