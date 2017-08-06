#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('1.1.1.1'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='')
print(" [x] Sent 'Hello World!'")
