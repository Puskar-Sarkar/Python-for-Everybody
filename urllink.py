from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

count=0
total_sum=0

tags = soup('span')
for tag in tags:
    content=int(tag.contents[0])
    count+=1
    total_sum+=content
    
print('Count', count)
print('Sum ', total_sum)
