#!/usr/bin/env python

import socket
import sys

import argparse

host = 'localhost'

def echoClient(port):
    print("Youngs Echo Client")

    while (1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creat tcp socket
        serverAddr = (host, port)
        print("Connecting to %s port %s" % serverAddr)
        s.connect(serverAddr)
    
    
        try:
        #send data
            message = input('what would you like to echo:')
            print("sending: %s" %message)
            s.sendall(str.encode(message))
            #wait for response
            recvsize = 0
            size = len(message)
            while recvsize < size:
                data = s.recv(16)
                recvsize += len(data)
                print("Recieved: %s " %data)
            message = ""
        except socket.errno as e:
            print("Socket error: %s" %str(e))
        except Exception as e:
            print("Other exception: %s" %str(e))
        except KeyboardInterrupt:
            s.close()
            break
        finally:
            s.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='youngs echo client')
    parser.add_argument('--port', action="store", dest="port", type=int, required = True)
    given_args = parser.parse_args()
    port = given_args.port
    echoClient(port)
        
