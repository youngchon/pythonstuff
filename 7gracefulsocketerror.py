#!/usr/bin/env python
#handling socket errors

import sys
import socket
import argparse

def main():
    #setup arg passing
    parser = argparse.ArgumentParser(description='Socket Error Ex')
    parser.add_argument('--host', action="store", dest="host", required=False)
    parser.add_argument('--port', action="store", dest="port", type=int, required=False)
    parser.add_argument('--file', action="store", dest="file", required=False)
    givenArgs = parser.parse_args()

    #args should loaded and saved

    givenArgs = parser.parse_args()
    host = givenArgs.host
    port = givenArgs.port
    filename = givenArgs.file

    #first try to make a socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print("Error creating socket: %s" %e)
        sys.exit(1)

    #second try to connect to host/ort
    try:
        s.connect((host,port))
    except socket.gaierror as e:
        print("Address-related eror connecting to a server: %s" %e)
        sys.exit(1)
    except socket.error as e:
        print("Connection error: %s" %e)
        sys.exit(1)

    #thrid try to send data
    
    try:
        mstr = "GET " + filename + "http/1.0\r\n\r\n"
        s.sendall(str.encode(mstr))
    except socket.error as e:
        print("Error sending data: %s" % e)
        sys.exit(1)

    while 1:
        #fourth try waiting to recieve data
        try:
            buf = s.recv(2048)
        except socket.error as e:
            print("error recving data: %s" % e)
            sys.exit(1)
        if not len(buf):
            break
        print(buf)

if __name__ == '__main__':
    main()
