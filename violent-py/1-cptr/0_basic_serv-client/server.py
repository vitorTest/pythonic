# Save as server.py 
# Message Receiver
import os
from socket import *
host = ""
port = 13000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)

response = ""

print("Waiting to receive messages...")	
while True:
    (data, addr) = UDPSock.recvfrom(buf)
    response += data.decode()
    print("Received message: " + response)
    if response == "exit":
        break
    response = ""

UDPSock.close()
os._exit(0)