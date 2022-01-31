from scapy.all import *
import csv

print("Reading pcap")
packets = PcapReader('ntpflood.pcap')
print("Completed reading pcap")

#pkt=packets[4]
#print(dir(pkt))
#?print(pkt.show())

#print(pkt[NTP].srcaddr)
#print(pkt[3].version)


f = open('NTP_ver_020122.csv','a')
count = 0


for packet in packets:
    if packet.haslayer("NTP") and packet[2].sport==123 and packet[1].dst=="128.232.21.75":
        src = packet[1].src
        dst = packet[1].dst
        sport = packet[2].sport  
        ver = packet[3].version
        #print(src, sport, ver)
        row = "\n"+src+', '+str(sport)+', '+dst+', '+str(ver)
        print(row)
        f.write(row)
        count += 1
        #print(count)
f.close()
print("Done!")

