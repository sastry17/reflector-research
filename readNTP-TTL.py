
from scapy.all import *
import csv
import gzip
import shutil
import argparse
import os



#pkt=packets[4]
#print(dir(pkt))
#?print(pkt.show())

#print(pkt[NTP].srcaddr)
#print(pkt[3].version)


f = open('NTP_metadata.csv','a')
#count = 0
def readpcap(file):
    with gzip.open(file, 'rb') as f_in:
        with open('temp.pcap', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    print("Reading pcap")
    packets = PcapReader('temp.pcap')
    print("Completed reading pcap")

    for packet in packets:
        if packet.haslayer("NTP") and packet[2].sport==123:
            try:

                #if packet.haslayer("NTP") and packet[2].sport==123 and (packet[3].precision == 0 or packet[3].delay ==0 or packet[3].dispersion==0):
                src = packet[1].src
                #dst = packet[1].dst
                ttl = packet[1].ttl
                sport = packet[2].sport 
                ver = packet[3].version
                strata =  packet[3].stratum
                timediff = 999
                

                try:

                    timediff =  int(packet[3].recv) - int(packet[3].sent)
                  
                
                except TypeError as e:
                    pass

                # if packet[3].recv is not None:
                #     recvtp = int(packet[3].recv)
                # else:
                #     recvtp = "None"
                    

                recvtp = str(packet[3].recv)
                ids = str(packet[3].id)
                #precision = packet[3].precision
                #delay= packet[3].delay
                #dispersion = packet[3].dispersion
                #orig = packet[3].orig
                #packet.show()
                #print(src,ttl,ver)
                row="\n"+src+", "+ids+", "+str(strata)+", "+str(ttl)+", "+str(ver)+", "+str(timediff)
                #print(src, sport, ver)
                #row = "\n"+src+', '+str(sport)+', '+dst+', '+str(precision)+', '+str(delay)+', '+str(dispersion)+', '+str(orig)
                print(row)
                f.write(row)
                #count += 1
                #print(count)
            except ValueError and AttributeError:
                pass
    f.close()
    os.remove('temp.csv')
    print("Done!")


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", required=True)
args = parser.parse_args()
filename=args.file
print(filename)
readpcap(filename)
