# this is the tutorials of RabbitMQ
# encoding=utf8

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# The messages will be lost if no queue is bound to the exchange yet, but that's okay for us; if no consumer is listening yet we can safely discard the message.
channel.exchange_declare(exchange='logs',type='fanout')

# Temporary queues 
# 1.let the server choose a random queue name for us. We can do this by not supplying the queue parameter to queue_declare:
# 2.once we disconnect the consumer the queue should be deleted,There's an exclusive flag for that:
# So it should be used like this 
queue_declared_result = channel.queue_declare(exclusive=True)

queue_name = queue_declared_result.method.queue
print queue_name

# Bind the queue and exchange
channel.queue_bind(exchange='logs',queue=queue_name)

print ' [*] Waiting for logs. To exit press CTRL+C'

def callback(ch, method, properties, body):
	print " [x] %r" % (body,)
channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)
channel.start_consuming()
