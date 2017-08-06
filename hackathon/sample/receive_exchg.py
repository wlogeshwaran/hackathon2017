#!/usr/bin/env python
import pika, re, os

connection = pika.BlockingConnection(pika.ConnectionParameters(host='1.1.1.1'))
channel = connection.channel()

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='hbd', queue=queue_name)

def callback(ch, method, properties, body):
      #print(" [x] Received %r" % body)
      #node_num=re.search("node=(\\d+)",body).group(1)
      #print("Node num is {}".format(node_num))
      #os.system("python ../processess/getStatus.py "+node_num)
      pass

channel.basic_consume(callback, queue=queue_name, no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

