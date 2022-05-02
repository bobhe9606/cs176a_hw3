from socket import *
import sys
import time


serverName = sys.argv[1]
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1) #wait at most 1 second before timeout
icmp_seq = 1
rttList = []
while (icmp_seq < 11):
    timeStamp = time.time()

    message = "PING {} {}".format(icmp_seq, timeStamp)
    clientSocket.sendto(message.encode(), (serverName, serverPort))

    try:
        serverMessage, serverAddress = clientSocket.recvfrom(2048)
        rtt = time.time() * 1000 - timeStamp * 1000
        rttList.append(rtt)
        print("PING received from {}: seq#={} time={} ms".format(
        serverName, icmp_seq, round(rtt, 3)))
        time.sleep(1)  # 1 second delay between each ping as per instructions
    except timeout:
        #in case of timeout, then there is already a 1 second delay before sending next ping
        print("Request timeout for seq#={}".format(icmp_seq))

    icmp_seq += 1

clientSocket.close()


#Reference: https://www.geeksforgeeks.org/find-average-list-python/
print("--- ping statistics ---")
packetsRcvd = len(rttList)
packetsPercentLost = (10 - packetsRcvd)  * 10
if packetsRcvd > 0:
    minRtt = min(rttList)
    maxRtt = max(rttList)
    avgRtt = sum(rttList) / packetsRcvd
    #Reference: https://stackoverflow.com/questions/1995615/how-can-i-format-a-decimal-to-always-show-2-decimal-places
    print("10 packets transmitted, {} received, {}% packet loss rtt min/avg/max = {:.3f} {:.3f} {:.3f} ms".format(
        packetsRcvd, packetsPercentLost, minRtt, avgRtt, maxRtt))
else:
    print("10 packets transmitted, 0 received, 100% packet loss"); 






