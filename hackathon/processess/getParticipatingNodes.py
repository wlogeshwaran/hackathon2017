import pika, re, os, time, pickle

connection = pika.BlockingConnection(pika.ConnectionParameters(host='1.1.1.1'))
channel = connection.channel()

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='hbd', queue=queue_name)

startTime = time.time()
nodes = {}

def formNodeTable(nodeId):
    global nodes
    nodes[nodeId] = {"state":"Active","MRS":1}

def timer():
    global nodes
    if time.time() - startTime > 20:
        f1=open('../participatingNodes.pkl', 'wb')
        pickle.dump(nodes, f1)
        f1.close()
        exit(0)

def callback(ch, method, properties, body):
    #print(" [x] Received %r" % body)
    node_num=body
    timer()
    formNodeTable(node_num)

channel.basic_consume(callback, queue=queue_name, no_ack=True)

print(' [*] Waiting for Heartbeats. ')
channel.start_consuming()
