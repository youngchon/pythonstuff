#!/usr/bin/env python
#ip address format practice

import socket
from binascii import hexlify #hexlify helps represent binary data in hex

def basicLocalHostInfo():
    hostName = socket.gethostname()
    ipAddress = socket.gethostbyname(hostName)
    print("Host name: %s" % hostName)
    print("IP address: %s" % ipAddress)

def remoteHostInfo():
    remoteHost = 'www.google.com'
    try:
        print ("Attempting to get the hostinfo of google")
        print ("IP Address: %s" %socket.gethostbyname(remoteHost))
    except socket.error as err_msg:
        print("%s : %s" %(remoteHost, err_msg))

def convertIP4Address():
    for ipaddr in ['127.0.0.1', '192.168.0.1']:
        packedIPAddr = socket.inet_aton(ipaddr)
        unpackedIPAddr = socket.inet_ntoa(packedIPAddr)
        print("IPAddress : %s -> packed: %s, unpacked: %s"\
              %(ipaddr, hexlify(packedIPAddr), unpackedIPAddr))


if __name__ == "__main__": #refrdesher, multimodule, you need this
    print("Youngs thir networking program in python")
    convertIP4Address()
