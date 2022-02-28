from scapy.all import *
import csv

print("Reading pcap")
packets = PcapReader('honeyntp.pcap')
print("Completed reading pcap")

#pkt=packets[4]
#print(dir(pkt))
#?print(pkt.show())

#print(pkt[NTP].srcaddr)
#print(pkt[3].version)


f = open('NTP_honeypot_021221.csv','a')
#count = 0


for packet in packets:
    if packet.haslayer("NTP") and packet[2].sport==123 and packet[1].dst=='':
    #if packet.haslayer("NTP") and packet[2].sport==123 and (packet[3].precision == 0 or packet[3].delay ==0 or packet[3].dispersion==0):
        src = packet[1].src
        dst = packet[1].dst
        ttl = packet[1].ttl
        sport = packet[2].sport  
        precision = packet[3].precision
        delay= packet[3].delay
        dispersion = packet[3].dispersion
        orig = packet[3].orig
        packet.show()
        #print(src, sport, ver)
        row = "\n"+src+', '+str(sport)+', '+dst+', '+str(precision)+', '+str(delay)+', '+str(dispersion)+', '+str(orig)
        #print(row)
        #f.write(row)
        #count += 1
        #print(count)
#f.close()
print("Done!")

