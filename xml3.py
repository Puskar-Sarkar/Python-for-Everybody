import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_2205816.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')
nums = list()
count=0
y=0
for result in counts:
    # Debug print the data :)
    #print(result.text)
    x=int(result.text)
    y+=1
    count+=x
    #print(x)
    #print(count)
    
print('Count:', y)
print('Sum:', count)