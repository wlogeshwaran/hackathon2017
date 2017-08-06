import subprocess, time

proc = subprocess.Popen(['python', '../sample/send_exchg.py']) 
print "starting send_exchg - %d"%proc.pid

proc = subprocess.Popen(['python', '../processess/getParticipatingNodes.py'])
print "Forming the cluster by identifying the participating nodes"
time.sleep(40)

proc = subprocess.Popen(['python', '../sample/receive_exchg.py'])
print "starting receive_exchg - %d"%proc.pid

proc = subprocess.Popen(['python', '../processess/conductElection.py'])
print "Electing the Active MCN and standby MCN %d"%proc.pid
'''
proc = subprocess.Popen(['python', '../sample/send_controlNode_status.py'])
print "Starting send MCN status %d"%proc.pid
proc = subprocess.Popen(['python', '../sample/receive_controlNode_status.py'])
print "Starting receive MCN status %d"%proc.pid
'''
