# this is the tutorials of RabbitMQ
#encoding=utf8
import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='taskq',durable=True)
message = ' '.join(sys.argv[1:]) or "Hello World!"

# !!Marking messages as persistent doesn't fully guarantee that a message won't be lost. Although it tells RabbitMQ to save message to the disk, there is still a short time window when RabbitMQ has accepted a message and hasn't saved it yet. Also, RabbitMQ doesn't do fsync(2) for every message -- it may be just saved to cache and not really written to the disk. The persistence guarantees aren't strong, but it's more than enough for our simple task queue. If you need a stronger guarantee you can wrap the publishing code in a transaction.

channel.basic_publish(exchange='',routing_key='taskq',body=message,
		      properties=pika.BasicProperties(
			delivery_mode = 2,# Make message persistent!
		     ))

print "[x] sent %r "%(message,)

connection.close()

