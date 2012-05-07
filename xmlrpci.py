#!/usr/bin/python
# encoding=utf8
# Filename:xmlrpci.py
import xmlrpclib,sys

url ='http://localhost:8100'
server = xmlrpclib.ServerProxy(url,allow_none=True)
#multicall = xmlrpclib.MultiCall(server)
print 'fetch avilable methods...'

"""
methods = server.system.listMethods()
while 1:
	print "\n\nAvailable Methods:"
	for i in range(len(methods)):
		print "%2d: %s" % (i+1,methods[i])
	selection = raw_input("Select one (q to quit):")
	if selection == 'q':
		break
	item = int(selection) - 1
	print "\n***********"
	print "Details for %s\n" % methods[item]
	
	for sig in server.system.methodSignature(methods[item]):
		print "Args: %s; Returns : %s" %(",".join(sig[1:]),sig[0])
	print "Help:",server.system.methodHelp(methods[item])
"""

print server.add(3,3)
print server.pow(2,2)
try:
    server.sendback("o.0 0.o")
except xmlrpclib.Fault, err:
    print "A fault occurred"
    print "Fault code: %d" % err.faultCode
    print "Fault string: %s" % err.faultString

