#!/usr/bin/python
import pickle

f1=open('participatingNodes.pkl', 'rb')
nodes = pickle.load(f1)
f1.close()

f1 = open("../mystate")
m = f1.read()
f1.close()


f1 = open("../partnerstate")
p = f1.read()
f1.close()


if len(m) > 1:
    print "===== Control Node Status ===="
    print "%s\t%s\tControl,Compute"%(m[0],m[1:])
    print "%s\t%s\tControl,Compute"%(p[0],p[1:])


print "\n\n===== Node Status ====="
for node, details in nodes.items():
    print "%s\t%s"%(node, details["state"])
