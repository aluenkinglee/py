#!/usr/bin/python
# encoding=utf8
# simplerpcserver example
from SimpleXMLRPCServer import SimpleXMLRPCServer,SimpleXMLRPCRequestHandler
from SocketServer import ForkingMixIn

class Math:
	def pow(self,x,y):
		return x**y
	def sendback(self,msg):
		print msg
class ForkingServer(ForkingMixIn,SimpleXMLRPCServer):
	pass
def add(x,y):
	return x+y

serveraddr =('',8100)
server = ForkingServer(serveraddr,SimpleXMLRPCRequestHandler, allow_none=True)
server.register_instance(Math())
server.register_introspection_functions()
server.register_function(add) 
print "[x] Waiting ..."
server.serve_forever()

