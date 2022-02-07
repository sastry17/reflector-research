import pandas as pd
import argparse

def filter_data(filename):
    input_data = pd.read_csv(filename,compression="gzip",sep=",", names=["saddr","sport","daddr","dport","classification","icmp_unreach_str","icmp_code","icmp_type","icmp_responder","success"], usecols=['saddr','sport','classification'])
    df=input_data.loc[input_data['classification']=="udp"]
    print("udp filter done")
    df.drop_duplicates("saddr",keep=False, inplace=True)
    #df=input_data.loc[input_data['saddr']!="202.232.184.169"]
    udf=df[['saddr','sport']]
    print("File loaded to dataframe")
    #print(udf)
    
    newfile=filename[30:-4]+'-ntp-hosts.txt'
    udf.to_csv(newfile, header=None, index=None,  mode='a')
    print(newfile)
    print("Done!")

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", required=True)
args = parser.parse_args()
filename=args.file
print(filename)
filter_data(filename)