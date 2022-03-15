from asyncore import read
import pandas as pd
import argparse
from scapy.all import *
import csv
import subprocess




def ungzip(filename):
    subprocess.run()


    count_amps(pcapfile)
    subprocess.run("[gzip]", "[-d]", filename)
    pcapfile = 





def count_amps(pcapfile):
    print("Reading pcap")
    packets = PcapReader(pcapfile)
    print("Completed reading pcap")
    newfile=+pcapfile[30:-4]+'-NTP-Mega-hosts.txt'
    df = pd.DataFrame()



    for packet in packets:
        if packet.haslayer("NTP") and packet[2].sport==123 and packet[1].dst=='':
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
            df.insert(row)
            df=df.groupby(df.columns.tolist(),as_index=False).size()
            df.to_csv(newfile, header=None, index=None,  mode='a')
        #print(row)
        #newfile.write(row)
        #count += 1
        #print(count)
    newfile.close()
    print("Done!")

#pkt=packets[4]
#print(dir(pkt))
#?print(pkt.show())

#print(pkt[NTP].srcaddr)
#print(pkt[3].version)




#count = 0




parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", required=True)
args = parser.parse_args()
filename=args.file
print(filename)
ungzip(filename)
