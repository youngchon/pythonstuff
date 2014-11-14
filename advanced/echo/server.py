#!/usr/bin/env python
#echo server

import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048
backlog = 5

def echoServer(port):
    print("Young's simple echo server")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reusable socket
    serverAddr = (host, port)
    s.bind(serverAddr)
    
    #start listening
    s.listen(backlog)
    
    while True:
        print("Waiting to recieve message from client")
        client, address = s.accept() #once a socket connection established
        data = client.recv(data_payload)
        if data:
            print ("Data: %s" %data)
            client.send(data)
            print ("Sent %s bytes back to %s" % (data, address))
        client.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='YoungsEchoServer')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echoServer(port)
