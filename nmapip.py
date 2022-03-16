from cmath import e
from xdrlib import Error
import nmap
import argparse



def scan(file):
    f = open(file, 'r')
    s = open("nmapOut.csv",'w')
    hostsl = f.readlines()
    print("read complete!")
    for line in hostsl:
        try:
            line=line.strip()
            nm = nmap.PortScanner()
            nm.scan(hosts=line, arguments='-sU -sT')
            print(line)
            
            #print(nm[line].state())           
            #print(nm.scaninfo())
            #print(isinstance(nm.all_hosts(),bool))
            
            for ip in nm.all_hosts():
                #print(ip)
                #print('----------------------------------------------------')
                #print('Host : %s (%s)' % (host, nm[host].hostname()))
                #print('State : %s' % nm[host].state())
                
                for proto in nm[ip].all_protocols():
                    try:
                        #print('----------')
                        #print('Protocol : %s' % proto)
                        lport = nm[ip][proto].keys()
                        
                        #print(lport.csv)
                        #lport.sort()
                        for port in lport:
                            #print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
                            pname=nm[ip][proto][port]['name']
                            #row =  str("\n"+host+", "+proto+", "+str(port)+", "+pname)
                            row =  "\n"+ip+", "+str(port)+", "+proto+", "+pname
                            s.write(row)
                            #print(row)
                    except Error as e:
                        print(e)
                        pass
        except Error as e:
            print(e)
            pass

    s.close()
    




parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", required=True)
args = parser.parse_args()
filename=args.file
print(filename)
scan(filename)