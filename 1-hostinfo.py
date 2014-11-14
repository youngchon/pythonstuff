#!/usr/bin/env python

import socket

def basicLocalHostInfo():
    hostName = socket.gethostname()
    ipAddress = socket.gethostbyname(hostName)
    print("Host name: %s" % hostName)
    print("IP address: %s" % ipAddress)

if __name__ == "__main__": #refresher, multimodule, you need this
    print("Youngs first networking program in python")
    basicLocalHostInfo()
