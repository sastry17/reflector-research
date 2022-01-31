set -e

# Run tcpdump to collect data in the form of a pcap that records the replies we get back from the zmap scan
# The & informs the shell to put the command in the background
sudo tcpdump -U -nni eth0 'dst host 128.232.21.75 and (src port 123 or icmp[icmptype] == icmp-unreach)' -w "/local/data/ip358/regularScans/NTP/ntp_dstIP_filtered_capture-$(dat>

sleep 5
#sudo zmap -T 2 --bandwidth=25M -p 123 -M udp --blacklist-file=/home/ip358/blacklist.txt --probe-args=file:/home/ip358/ntp_123.pkt -o "/local/data/ip358/regularScans/NTP/zmapN>

sudo zmap -T 2 --bandwidth=25M -v 5 -M udp -p 123 --output-module=csv --blacklist-file=/home/ip358/blacklist.txt --probe-args=file:/home/ip358/ntp_123.pkt -f "saddr,sport,dadd>

# This line kills the background job - tcpdump - upon the completion of zmap - http://tldp.org/LDP/abs/html/x9644.html
# kill %1
# kill the most recently started background job - https://unix.stackexchange.com/questions/460090/centos-background-processes
#sudo kill "$!" 

pid=$(ps -e | pgrep tcpdump)
sleep 5
sudo kill $pid

# Copy results to S6, and clear files on CCC scanner
echo "Zmap scan complete, now copying results to S6."
sudo gzip /local/data/ip358/regularScans/NTP/*.{pcap,txt}
sudo -H -u ip358 scp /local/data/ip358/regularScans/NTP/*.gz ip358@shalmaneser9.sec.cl.cam.ac.uk:/home/ip358/regularScans/NTP/
sudo rm /local/data/ip358/regularScans/NTP/*.gz
echo "NTP script finished." 

