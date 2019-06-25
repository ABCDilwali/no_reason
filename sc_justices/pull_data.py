import requests
from bs4 import BeautifulSoup
import re
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}


url='https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exlimit=20&redirects=1&titles=List%20of%20law%20schools%20attended%20by%20United%20States%20Supreme%20Court%20Justices'
# https://stackoverflow.com/questions/7638402/how-to-get-infobox-from-a-wikipedia-article-by-mediawiki-api
base_url='https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=json&titles={}&rvsection=0'


def get_soup(url):
        x=requests.get(url, headers=headers, verify=False)
        soup = BeautifulSoup(x.content, "html.parser")
        return soup

soup1=get_soup(url)
lis=soup1.find_all('li')

i=0
for li in lis:
    children=li.findChildren('li')
    for child in children:
        i+=1    
        #print(li.text.split('\\n')[0],'---', len(children),'---', child.text)
        child_url=base_url.format(child.text)
        #print(url)
        child_soup = get_soup(child_url)
        cs1=child_soup.text[child_soup.text.find('{{Infobox')+2:]
        cs1=cs1[0:cs1.find('\\n}}')]
        cs1=cs1.replace('[','').replace(']','')
        cs1=re.sub(pattern='\|(?=.{2,3}\))',repl='<>',string=cs1)
        cs1=re.sub(pattern='\|(?=[^\{]*\})',repl='<>',string=cs1)
        print(child.text)
        for x in cs1.split('|'):
            print('---'.join([y.replace('\\n','') for y in x.split('=')]))
        if i>3: break
    if i>3: break



cs1
