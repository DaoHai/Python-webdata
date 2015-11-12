import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter Location:')
print 'Retrieving:', url
uh = urllib.urlopen(url) 
data = uh.read()
print 'Retrieved',len(data),'characters'

tree = ET.fromstring(data)
lst = tree.findall('comments/comment')

print 'Count:', len(lst)

sum=0

for item in lst:
	sum=sum+int(item.find('count').text)

print 'Sum:', sum


