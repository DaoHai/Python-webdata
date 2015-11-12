# Note - this code must run in Python 2.x 
#loop over embeded links

import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
count = raw_input('Enter count: ')
count=int(count)
position = raw_input('Enter position: ')
position=int(position)

for iters in range(count+1):
	if iters==count:
		print 'Last URL:', url
	else:
		print 'Retrieving:', url

	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	# Retrieve all of the anchor tags
	tags = soup('a')
        url= tags[position-1].get('href', None)
	
	   

