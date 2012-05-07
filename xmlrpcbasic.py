#!/usr/bin/python
# encoding=utf8
# Filename : xmlrpcbasic.py
import xmlrpclib,sys
url = 'localhost:8765'
s = xmlrpclib.ServerProxy(url)
catdata = s.meerkat.getCategories()
cattitles = [item['title'] for item in catdata]
cattitles.sort()
for item in cattitles:
	print item

