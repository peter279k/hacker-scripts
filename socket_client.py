#!/usr/bin/python3

import socket
import argparse

parser = argparse.ArgumentParser(description='Please input the port numbers')
parser.add_argument('--ports', metavar='Y', type=str, help='Please use 3306,80,21 to add ports lists')
parser.add_argument('--url', metavar='Y', type=str, help='Please set a target URL or IP address')

args = parser.parse_args()

if args.ports is None:
    print('Please input following ports: 3306,80,21... and so on.')
    exit(1)

ports = args.ports
ports_list = ports.split(',')

ip_address = args.url

if ip_address is None:
    print('Please set the targeted URL or IP address via --url option')
    exit(1)

for port_number in ports_list:
    try:
        int(port_number)
    except:
        print('The port number %s is invalid. Skipped' % port_number)
        continue

    s = socket.socket()
    try:
        s.connect((ip_address, int(port_number)))
        answer = "Answer for " + str(port_number) + ":"
        print(answer)
        print(s.recv(1024))
    except:
        answer = "No anaswer for " + str(port_number)
        print(answer)

    print("")
