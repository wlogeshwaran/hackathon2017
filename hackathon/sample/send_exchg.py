#!/usr/bin/env python
import pika
import time
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('1.1.1.1'))
channel = connection.channel()
channel.exchange_declare(exchange='hbd', type='fanout')

with open("../nodeDetails") as fp:
    nodeDetail=json.load(fp)
i=0
while True:
#    channel.basic_publish(exchange='hbd', routing_key='', body=str(nodeDetail["slotId"]))
    i = i + 1
    channel.basic_publish(exchange='hbd', routing_key='', body=str(nodeDetail["slotId"]))
    #print "sent hbd {}".format(nodeDetail["slotId"])
    time.sleep(.5)
