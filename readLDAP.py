from scapy.all import *
import csv

print("Reading pcap")
packets = PcapReader('/home/ip358/regularScans/LDAP/ldap_dstIP_filtered_capture-+2022-03-19T022901.pcap.gz')
print("Completed reading pcap")

##pkt=packets[4]
#print(dir(pkt))
#print(pkt.show())

#print(pkt[NTP].srcaddr)
#print(pkt[3].version)


f = open('LDAP_amazon_HP.csv','a')
#count = 0

search = b'Access Forbidden'


for packet in packets:
    #packet.show()
    #print(str(packet.time))
    if packet.haslayer("UDP") and packet[2].sport==389:
    #if packet.haslayer("NTP") and packet[2].sport==123 and (packet[3].precision == 0 or packet[3].delay ==0 or packet[3].dispersion==0):
        src = packet[1].src
        dst = packet[1].dst
        ttl = packet[1].ttl
        sport = packet[2].sport
        if search in packet[3].load:
            row = "\n" +  src + ', ' + str(packet.time) + ', ' + 'amazon-hp'
        else:
            row = "\n" +  src + ', ' + str(packet.time) + ', ' + 'non-amazon-hp'
        #precision = packet[3].precision
        #delay= packet[3].delay
        #dispersion = packet[3].dispersion
        #orig = packet[3].orig
        #packet.show()
        #print(src, sport, ver)
        #row = "\n"+src+', '+str(sport)+', '+dst+', '+str(precision)+', '+str(delay)+', '+str(dispersion)+', '+str(orig)
        #print(row)
        f.write(row)
        #count += 1
        #print(count)
f.close()
print("Done!")

