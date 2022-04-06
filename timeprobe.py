
from socket import AF_INET, SOCK_DGRAM
import sys
import socket
import struct, time
import argparse
from scapy.all import *


def getNTPTime(host):
        port = 123
        buf = 43008
        address = (host,port)
        msg = '\x1b' + 47 * '\0'
        mon = '\x1b\x00\x00\x00'+'\x00'*11*4

        # reference time (in seconds since 1900-01-01 00:00:00)
        TIME1970 = 2208988800 # 1970-01-01 00:00:00

        #socket.setSoTimeout(10000);
        
            

        # connect to server
        try:
            client = socket.socket( AF_INET, SOCK_DGRAM)
            client.sendto(msg.encode('utf-8'), address)
            #client.sendto(mon.encode('utf-8'), address)

            client.settimeout(2)

            msg, address = client.recvfrom( buf )

            if msg is not None:
                #print(address)
                #print(msg)
                #pkt_hex = UDP(import_hexcap(msg))
                #print('Hex',pkt_hex)
                #new_pkt = pkt_hex.__class__(pkt_hex)
                #new_pkt.show()
                #pkt=msg[0]
                #npacket=UDP[pkt]
                #U.show()
                t = struct.unpack( "!12I", msg )[10]
                print(host, t)
                #print(t)
                #msg.show()
            else:
                print('no response')
        except socket.timeout:
            print(ip,"timeout")


        #t -= TIME1970
        #return time.ctime(t).replace("  "," ")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--IP", required=True)
    args = parser.parse_args()
    ip=args.IP
    ip=ip.rstrip()
    #print(ip)
    getNTPTime(ip)
