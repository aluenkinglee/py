# this is the tutorials of RabbitMQ
#encoding=utf8

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch,method,properties,body):
	print '[x] Received %r' % (body,)

def on_request(queue):
	method_frame, header_frame, body = channel.basic_get(queue='hello')
	if method_frame.NAME == 'Basic.GetEmpty':
		print 'Receive empty msg.'
	else:
		print body
		channel.basic_ack(delivery_tag=method_frame.delivery_tag)
on_request('hello')

#channel.basic_consume(callback,queue = 'hello',no_ack = True)
#channel.start_consuming()
