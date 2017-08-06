#!/usr/bin/env python
import pika
import time
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('1.1.1.1'))
channel = connection.channel()
channel.queue_declare(queue='hello')

with open("../nodeDetails") as fp:
    nodeDetail=json.load(fp)

while True:
    channel.basic_publish(exchange='', routing_key='hello', body=str(nodeDetail["slotId"]))
    print "sent hbd {}".format(nodeDetail["slotId"])
    time.sleep(.5)
