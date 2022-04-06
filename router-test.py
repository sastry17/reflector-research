# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 10:14:51 2022

@author: JG07DA
"""

from socket import AF_INET, SOCK_DGRAM
import sys
import socket
import struct, time
import argparse
from scapy.all import *

#i = IP()
#i.dst='49.143.20.1'

#p = UDP()
#p.dport="123"

#ans, uns = sendp(i/u,count=10,timeout=2)
#ans, uans = sr(IP(dst="49.143.20.1")/UDP(sport=123,dport=(123)/Raw(load='\x1b' + 47 * '\0'),count=10,timeout=2))

#request = (IP(dst="49.143.20.1")/UDP(sport=123,dport=("123")/Raw(load='\x1b' + 47 * '\0')),count=10,timeout=2)

#request.show()


#ntpip = "105.100.85.223"

# monlist -> (load=str("\x17\x00\x03\x2a")+ str("\x00")*4)
#ntp -> (load=str('\x1b') + 47 * str('\0')


def router_test(file):
    port = 123
    buf = 43008
    
    msg = '\x1b' + 47 * '\0'
    msg=msg.encode('utf-8')
    mon = '\x1b\x00\x00\x00'+'\x00'*11*4
    f = open(filename, 'r') 
    newfile=filename+"router_test_p1.csv"
    s =open(newfile,'w')
    for line in f:
        ip = line.rstrip()
        print(ip)
        address = (ip,port)
        count = 0
        pct = 0
        while count<9:
            try:
                #pct=0
                client = socket.socket( AF_INET, SOCK_DGRAM)
                client.sendto(msg, address)
                client.settimeout(2)
                msg, address = client.recvfrom( buf )

                if msg is not None:
                    pct=pct+1
                    #print(pct)
                    count = count+1
                    #print(count)
                
            except socket.timeout:
                    count = count+1
                    #print(count)
        
        #packet = IP(dst=ip)/UDP(sport=123,dport=123)/("\x1b\x00\x00\x00"+"\x00"*11*4)
        #packet.show()
        #ans= sr1(packet,timeout=2)
        #if ans is not None:
        #    row = "\n"+ip+", "+ans[0][1].len
        #else:
        #    row = "\n"+ip+", "+"NA"
        print(pct)
        row=('\n'+ip+', '+str(count)+', '+str(pct))
        s.write(row)
    s.close()

#ans, uans = send(packet,count=10)
#print(ans.summary())

#print(uans.summary)


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", required=True)
args = parser.parse_args()
filename=args.file
print(filename)
router_test(filename)
