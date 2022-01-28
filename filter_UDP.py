import pandas as pd
import argparse

def filter_data(filename):
    input_data = pd.read_csv(filename,sep=",", names=["saddr","sport","daddr","dport","classification","icmp_unreach_str","icmp_code","icmp_type","icmp_responder","success"]
, usecols=['saddr','classification'])
    df=input_data.loc[input_data['classification']=="udp"]
    udf=df[['saddr']]
    print("File loaded to dataframe")
    #print(udf)
    
    newfile=filename[:-4]+'-udp-hosts.txt'
    print(newfile)
    udf.to_csv(newfile, header=None, index=None,  mode='a')
    print("Done!")

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", required=True)
args = parser.parse_args()
filename=args.file
print(filename)
filter_data(filename)