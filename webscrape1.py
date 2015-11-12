import urllib

fhand=urllib.urlopen('http://www.vietnamnet.vn')
for line in fhand:
	print line.strip()
