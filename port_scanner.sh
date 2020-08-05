#!/bin/bash

nmap -sT 210.240.170.0/24 -p 3306 >/dev/null -oG MySQLScan

cat MySQLScan | grep open > MySQLScan2

cat MySQLScan2
