import pickle
import json


def election():

    f = open("participatingNodes.pkl", "rb")
    nodes = pickle.load(f)
    f.close()

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

    exit(0)

election()
