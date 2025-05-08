import urllib.request
import json
url = input('Enter location: ')
if len(url) < 1 :
    url = 'http://py4e-data.dr-chuck.net/comments_2205817.json'
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved',len(data),'characters')
info = json.loads(data)
comments = info['comments']
count = len(comments)
tot_sum = sum(comment['count'] for comment in comments)
print('Count:', count)
print('Sum:', tot_sum)