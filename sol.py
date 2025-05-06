import urllib.request
import xml.etree.ElementTree as ET
url = input("Enter location: ").strip()
print("Retrieving", url)
response = urllib.request.urlopen(url)
data = response.read()
print("Retrieved", len(data), "characters")
tree = ET.fromstring(data)
counts = tree.findall('.//count')
total = sum(int(count.text) for count in counts)
print("Count:", len(counts))
print("Sum:", total)