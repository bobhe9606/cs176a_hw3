from audioop import avg
from datetime import datetime
import random
from socket import *
from struct import pack
import sys
import time
from datetime import datetime

serverName = sys.argv[1]
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
icmp_seq = 0
rttList = []
while (icmp_seq < 11):
    timeStamp = time.time()
    # timeStamp = int(datetime.now())

    message = "PING {} {}".format(icmp_seq, timeStamp)
    clientSocket.sendto(message.encode(), (serverName, serverPort))

    try:
        serverMessage, serverAddress = clientSocket.recvfrom(2048)
        rtt = time.time() * 1000 - timeStamp * 1000
        rttList.append(rtt)
        # rtt = int(datetime.now() * 1000) - timeStamp * 1000
        print("PING received from {}: seq#={} time={} ms".format(
        serverName, icmp_seq, round(rtt, 3)))
    except timeout:
        print("Request timeout for seq#={}".format(icmp_seq))


    icmp_seq += 1

clientSocket.close()
#https://www.geeksforgeeks.org/find-average-list-python/
print("-- ping statistics --")
packetsRcvd = len(rttList)
packetsPercentLost = (10 - packetsRcvd)  * 10
minRtt = min(rttList)
maxRtt = max(rttList)
avgRtt = sum(rttList) / packetsRcvd
print("10 packets transmitted, {} received, {}% packet loss rtt min/avg/max = {} {} {} ms".format(packetsRcvd, packetsPercentLost, round(minRtt, 3), round(avgRtt, 3), round(maxRtt, 3)))






