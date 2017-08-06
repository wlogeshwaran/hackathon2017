#!/usr/bin/env python
import pika
import time
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('1.1.1.1'))
channel = connection.channel()
channel.exchange_declare(exchange='mcn', type='fanout')


with open("../initialActStanState") as fp1:
    mcnState = json.load(fp1)

with open("../nodeDetails") as fp2:
    myNodeDetails = json.load(fp2)

if myNodeDetails["slotId"] == mcnState["active"] or \
     myNodeDetails["slotId"] == mcnState["standby"]:

    while True:
        f3 = open("../partnerstate")
        partnerstate=f3.read()
        f3.close()
        channel.basic_publish(exchange='mcn', routing_key='', body=str(myNodeDetails["slotId"]))
        if partnerstate[1:] == "Failed":
            channel.basic_publish(exchange='mcn', routing_key='', body='%s DEAD'%partnerstate[0])
        print "sent hbd {}".format(myNodeDetails["slotId"])
        time.sleep(.5)
