#!/usr/bin/env python
#Author: jtoddp14 
#Updated February 25, 2018
from socket import * #Needed for the portscan itself    
import sys #Need to exit program

target = ''
portMax = 5000 #Set to whatever maximum is needed
portMin = 1 #Set to whatever minimum is needed

def targetScan(target, port, rCode = 1): #Establishes connection to host and target
	try:
		i = socket(AF_INET, SOCK_STREAM) #Initiates socket
		
		targetCheck = s.connect_ex((target, port))
		#Attempts to connect, then returns the result
		if targetCheck == 0: 
			rCode = targetCheck
		i.close()
	except Exception, e:
		pass
	
	return rcode

try: 
	target = raw_input("* Enter Target Address: ") #Sets target to scan
except KeyboardInterrupt:
	print("\n\n* User Abort...") #Stops scanning when user interrupts
	sys.exit(1)

targetIp = gethostbyname(target) #Fetches the targets IP by host name
print("\n* Target: %s IP: %s" % (target, targetIp)) 
print("* Starting Scan...")

for port in range(portMin, portMax):
	try:
		response = scanTarget(target, port) 
		
		if response == 0:
			print("* Port %d: Open" % (port)) #Tries every port in range and prints if the port is open
	except Exception, e:
		pass #Moves to the next port if port does not respond

print("\n* All Ports Scanned")

