# this is the tutorials of RabbitMQ
# encoding=utf8
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#  The durability options let the tasks survive even if RabbitMQ is restarted.
channel.queue_declare(queue='taskq',durable=True)

print ' [*] Waiting for messages. To exit press CTRL+C'
def callback(ch,method,properties,body):
	print '[x] Received %r' % (body,)
	# time.sleep(body.count('.'))
	print '[x] Done'
	# 添加相应
	ch.basic_ack(delivery_tag = method.delivery_tag)

#. This tells RabbitMQ not to give more than one message to a worker at a time. Or, in other words, don't dispatch a new message to a worker until it has processed and acknowledged the previous one. Instead, it will dispatch it to the next worker that is not still busy.

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,queue = 'taskq')
channel.start_consuming()
