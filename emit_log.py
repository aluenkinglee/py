# this is the tutorials of RabbitMQ
# encoding=utf8
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
# Producer can only send messages to an exchange.On one side it receives messages from producers and the other side it pushes them to queues. The exchange must know exactly what to do with a message it receives. 
# fanout : it just broadcasts all the messages it receives to all the queues it knows.
channel.exchange_declare(exchange='logs',type='fanout')
message = ' '.join(sys.argv[1:]) or "info:Hello world!"

# Nameless exchange: messages are routed to the queue with the name specified by routing_key, if it exists
channel.basic_publish(exchange='logs', 	# The exchange parameter is the the name of the exchange. 
			routing_key='',	# THE VALUE IS IGNORGED FOR FANOUT EXCHANGE
			body=message)

# ^-- The most important change is that we now want to publish messages to our logs exchange instead of the nameless one. We need to supply a routing_key when sending, but its value is ignored for fanout exchanges. 

print "[X] sent %r " % (message,)
connection.close()


