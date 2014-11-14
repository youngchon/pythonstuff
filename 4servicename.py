#!/usr/bin/env python
#network service information

import socket

def findServiceName():
    protocolname = 'tcp' #usingtcp
    for port in [80, 25]:
        print("Port: %s => service name: %s" %(port, socket.getservbyport(port, protocolname)))
    
    print("Port: %s via udp => serice nme: %s" %(53, socket.getservbyport(53,'udp')))

if __name__ == '__main__':
    findServiceName()
