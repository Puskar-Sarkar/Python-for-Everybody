import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

counts = int(input('Enter Count: '))
position = input('Enter Position: ')
print('Retrieving:',url)
for count in range(counts):
    pos = 0
    tags = soup('a')
    for tag in tags:
        content = tag.get('href',None)
        pos += 1
        if int(pos) == int(position):
            print('Retrieving:', content)
            url = content
            html = urllib.request.urlopen(url,context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
