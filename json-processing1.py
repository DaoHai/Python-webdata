import urllib
import json

url = raw_input('Enter Location:')
print 'Retrieving:', url
uh= urllib.urlopen(url)

input=uh.read() #string received
print 'Retrieved',len(input),'characters'


info = json.loads(input) #in form of json as a dictionary

x=info["comments"] #extract information about comments in form of a list of dictionary
print 'Count:', len(x)
sum=0

for item in x:
    sum=sum+int(item["count"])

print 'Sum:', sum


