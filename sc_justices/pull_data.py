import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}


url='https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exlimit=20&redirects=1&titles=List%20of%20law%20schools%20attended%20by%20United%20States%20Supreme%20Court%20Justices'

x=requests.get(url, headers=headers, verify=False)
soup = BeautifulSoup(x.content, "html.parser")
for li in soup.find_all('li'):
    if li.parent.name=='ol' or li.parent.name=='ul':
        print(li.text)
