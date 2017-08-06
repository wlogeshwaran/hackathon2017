#!/usr/bin/env python
import pika, re, os, json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='1.1.1.1'))
channel = connection.channel()

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='mcn', queue=queue_name)

f1 = open("../nodeDetails")
nodeDetail=json.load(f1)
f1.close()

f2 = open("../mystate")
mystate=f2.read()
f2.close()

f3 = open("../partnerstate")
partnerstate=f3.read()
f3.close()


thrsld = 10;#This global variable incresases whenever there is no msg from the partner. And resets to 0 when received.
thrsld_cnt = 0

def failThePartner():
    global f1, f2, f3, partnerstate, mystate
    if mystate[1:] == "Active":
        f3 = open("../partnerstate","w+")
        f3.write("%sFailed"%partnerstate[0])
        f3.close()

    if mystate[1:] == "Standby":
        print "Hi"
        f2 = open("../mystate","w+")
        f3 = open("../partnerstate","w+")
        f2.write("%sActive"%mystate[0])
        f3.write("%sFailed"%partnerstate[0])
        f2.close()
        f3.close()


def changePartnerState():
    global f1, f2, f3, partnerstate, mystate

    f3 = open("../partnerstate")
    partnerstate=f3.read()
    f3.close()

    if partnerstate[1:] == "Failed":
        f3 = open("../partnerstate","w+")
        f3.write("%sStandby"%partnerstate[0])
        f3.close()


def changeMyState():
    global f1, f2, f3, partnerstate, mystate

    f3 = open("../partnerstate")
    partnerstate=f3.read()
    f3.close()

    if partnerstate[1:] == "Standby":
        f3 = open("../partnerstate","w+")
        f3.write("%sActive"%partnerstate[0])
        f3.close()

    f2 = open("../mystate")
    mystate=f2.read()
    f2.close()

    if mystate[1:] == "Active":
        f2 = open("../mystate","w+")
        f2.write("%sStandby"%mystate[0])
        f2.close()


def lookForMCN(MCNnodeId):
    global thrsld_cnt, rebirth

    if int(MCNnodeId) != int(partnerstate[0]):
        thrsld_cnt = thrsld_cnt + 1
        if thrsld_cnt >= thrsld:
            print "Partner Failed"
            failThePartner()
    else:
        thrsld_cnt =0
        '''rebirth = rebirth + 1 if thrsld_cnt >= thrsld else 0
        if rebirth > 10:
            thrsld_cnt =0'''
        changePartnerState()
        '''if thrsld_cnt != 0:
            thrsld_cnt =thrsld_cnt - 1
            if thrsld_cnt == 0:
                changePartnerState()'''



def callback(ch, method, properties, body):
      global f1, f2, f3, partnerstate, mystate

      print(" [x] Received %r" % body)
      MCNnodeId = body
      if re.search("([1-9]) DEAD",MCNnodeId):
          deadNode = re.search("([1-9]) DEAD",MCNnodeId)

          if int(deadNode.group(1)) == int(mystate[0]):
              changeMyState()
      else:        
          lookForMCN(MCNnodeId)

channel.basic_consume(callback, queue=queue_name, no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()


