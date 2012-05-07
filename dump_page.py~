#!/usr/bin/python
# Filename : dump_page.py
import sys,urllib2
url = 'http://'+sys.argv[1]
req = urllib2.Request(url)
try:
	fd = urllib2.urlopen(req)
except  urllib2.URLError,e:
	print 'Error retrieving data:',e
	sys.exit(1)
while 1:
		data = fd.read(1024)
		if not len(data):
			break
		sys.stdout.write(data)
