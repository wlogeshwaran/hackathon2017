import pickle
f = open("participatingNodes.pkl", "rb")
k = pickle.load(f)
print k
f.close()
