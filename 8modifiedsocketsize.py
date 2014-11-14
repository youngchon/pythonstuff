#!/usr/bin/env python
#modifying send/recv sizes

import socket

SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

def modifyBuffSize():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #get the size of the socket's send buffer
    bufsize = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Buffer size [before]:%d" %bufsize)
    
    s.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    s.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_SNDBUF,
        SEND_BUF_SIZE)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUF_SIZE)
    bufsize = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Buffer size [after]:%d" %bufsize)

if __name__ == '__main__':
    modifyBuffSize();
