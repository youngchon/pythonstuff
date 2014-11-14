#!/usr/bin/env python
#converting intgerts to and from host to network byte order

import socket

def convertInt():
    data = 1337
    print("32 bit number (i.e. long)")
    print("Original: %s => long host byte order: %s, network byte order: %s"\
          %(data, socket.ntohl(data), socket.htonl(data)))
    print("16 bit number (i.e. short)")
    print("Original: %s => short host byte order : %s, network byte order: %s"\
          %(data, socket.ntohs(data), socket.htons(data)))

if __name__ == '__main__':
    print("Youngs integer to network conversion example")
    convertInt()
