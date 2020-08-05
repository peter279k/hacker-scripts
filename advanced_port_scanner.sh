#!/bin/bash

read -p "Please input your first IP address: " first_ip_addr
read -p "Please input your last IP address: " last_ip_addr
read -p "Please input your port number: " port

nmap -sT $first_ip_addr-$last_ip_addr -p ${port} >/dev/null -oG MySQLScan

cat MySQLScan | grep open > MySQLScan2

cat MySQLScan2
