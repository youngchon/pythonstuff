#!/usr/bin/env python
#moving on from a basic machine info
#find information from a remote host


import socket

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

if __name__ == "__main__": #refresher, multimodule, you need this
    print("Youngs second networking program in python")
    remoteHostInfo()
