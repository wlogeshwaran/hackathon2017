import time
import pickle
import json

#Sample state  [{'state': 'Active', 'id': 5, 'MRS':3}, {'state': 'Active', 'id': 1, 'MRS':1}] 
nodes = {}
allNodeIds = []
#nodeIds =['1','2','3','4','5','1','2','3','4','5','1','2','3','1','2','3','1','2','3']
nodeIds =['1','1','5','3','2','3','4','3','5','1','2','2','4','5','2','3','2','3','3','1','1','1','1','1','1','1','1','1']


def formNodeTable(nodeId):

    '''for node in nodes:
        allNodeIds.append(node["id"])'''
        
    nodes[i] = {"state":"Active","MRS":1}


def getState(i):
    for j, node in nodes.iteritems():
        node['MRS'] = node['MRS'] + 1; #increases the Message received Since flag. This flag will be set to 0 when the node Id is found in the queue. 

         
        if int(i) == int(j):
            node['MRS'] = 1
            node["state"] = "Active"
        if node['MRS'] >2*(len(nodes.keys())):
            node["state"] = "Failed"



def election():
    contestingNodes = []
    contestingNodes = nodes.keys()
    contestingNodes.sort()

    f = open("../initialActStanState","w+")
    f.write("{\"active\":%s,\"standby\":%s}"%(contestingNodes[0], contestingNodes[1]))
    f.close()

    with open("../nodeDetails") as fp:
      nodeDetail=json.load(fp)

    f = open("../mystate","w+")
    f2 = open("../partnerstate","w+")

    if int(nodeDetail["slotId"]) == int(contestingNodes[0]):
        f.write("%sActive"%contestingNodes[0])
        f2.write("%sStandby"%contestingNodes[1])
    elif int(nodeDetail["slotId"]) == int(contestingNodes[1]):    
        f.write("%sStandby"%contestingNodes[1])
        f2.write("%sActive"%contestingNodes[0])

    return (contestingNodes[0], contestingNodes[1])


#Node ids should be got from rabbit message queue

#time.sleep(60)
for i in nodeIds:
    formNodeTable(i)
f1=open('participatingNodes.pkl', 'wb')
pickle.dump(nodes, f1)
f1.close()

print nodes


for i in nodeIds:
    getState(i)

print nodes

#time.sleep(10)
a = election()
print a
