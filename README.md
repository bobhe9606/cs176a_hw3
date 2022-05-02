# Nicolas Johnson and Robert He

## PingClient:

UDP Client creates a UDP socket that has a set timeout of 1 second.  This means that if the client sends a message and it does not get a response within 1 second, the program will throw a timeout exception.  
UDP Client will loop 10 times to send 10 pings. Specifically, UDP client will send 10 messages of "PING {SEQUENCE NUMBER} {TIME STAMP}" to the UDP server.  Then, UDPClient will try to wait for the response.  If 1 second passes without a response, the UDP Client socket throws a timeout exception.  Otherwise, the UDP client would have received the response, so it records the round trip time.  Then the program will sleep for 1 second so that it waits approximately at least 1 second between each ping it sends to the server.

After the 10 pings, the UDP Client uses the recorded round trip times to calculate the ping statistics.

### Issues:
I noticed the gradescope autograder does not round down, and it requires there to always be 3 decimal places, even in the case of a number such as "1.000" where it needs 0's to fill in the 3 decimal places.  I had to look up on stack overflow how to use python's formatting to replicate this. 

### References:

- https://stackoverflow.com/questions/1995615/how-can-i-format-a-decimal-to-always-show-2-decimal-places
- https://www.geeksforgeeks.org/find-average-list-python/