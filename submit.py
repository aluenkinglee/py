#!usr/bin/python
import sys,urllib2,urllib

zipcode = sys.argv[1]
url = 'http://www.wunderground.com/cgi-bin/findweather/getForecast'
data = urllib.urlencode([('query',zipcode)])
print 'Using url:',url
print 'data:',data
try:
	req = urllib2.Request(url)
except urllib2.URLError,e:
	print "Error retrieving data:",e
	sys.exit(1)

fd = urllib2.urlopen(req,data)

while 1:
	data = fd.read(1024)
	if not len(data):
		break
	sys.stdout.write(data)
