#!/usr/bin/python3

import socket

ports = [22, 80, 443, 3306]

for port_number in ports:
    s = socket.socket()
    try:
        s.connect(('127.0.0.1', port_number))
        answer = "Answer for " + str(port_number) + ":"
        print(answer)
        print(s.recv(1024))
    except:
        answer = "No anaswer for " + str(port_number)
        print(answer)

    print("")
