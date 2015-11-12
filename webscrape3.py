#retrieve the webpage and extract required numbers

import urllib
from BeautifulSoup import *

#url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.html' 
html = urllib.urlopen('http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_197841.html').read()

soup = BeautifulSoup(html)


# Retrieve all of the anchor tags
tags = soup('span')
numsum=0

for tag in tags:
   # Look at the parts of a tag
   print 'TAG:',tag
   #print 'URL:',tag.get('href', None)
   print 'Contents:',tag.contents
   print type(tag.contents)
   num=[float(i) for i in tag.contents]
   print type(num)
   numsum=numsum+sum(num)


print 'RESULT:', numsum
