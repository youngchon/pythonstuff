#!/usr/bin/env python
#setting default timeouts

import socket

def socketTimeout():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Default socket timeout: %s" %s.gettimeout())
    s.settimeout(100)
    print("Current socekt timeout: %s" %s.gettimeout())

if __name__ == '__main__':
    socketTimeout()
