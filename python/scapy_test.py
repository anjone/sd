from scapy.all import *
import os

pkts = []
count = 0
pcapnum = 0

def write_cap(x):
    global pkts
    global count
    global pcapnum
    pkts.append(x)
    count += 1
    if count == 3:
        pcapnum += 1
        pname = "pcap%d.pcap" % pcapnum
        wrpcap(pname, pkts)
        pkts = []
        count = 0

def test_dumpfile():
    print("Testing the dump file...")
    dump_file = "./pcap1.pcap"
    if os.path.exists(dump_file):
        print("dump file %s found." % dump_file)
        pkts = sniff(offline=dump_file)
        count = 0
        while(count <= 2):
            print("------Dumping pkt:%s------" % count)
            print(hexdump(pkts[count]))
            count += 1
    else:
        print("Dump file %s not found." % dump_file)

def modify_packet_header(pkt):
    #print(hexdump(pkt))
    #print("--IP layer--: %s" % hexdump(pkt.getlayer(IP)))
    if pkt.haslayer(TCP): #and pkt.getlayer(TCP).dport == 80: #and pkt.haslayer(Raw):
        print(pkt[TCP].payload)
        print(dir(pkt[TCP].payload))
        #hdr = pkt[TCP].payload.__dict__
        #extra_item = {"Extra Header": "extra value"}
        #hdr.update(extra_item)
        #send_hdr = "\r\n".join(hdr)
        #pkt[TCP].payload = send_hdr

        #pkt.show()
        #print(hexdump(pkt))

        #del pkt[IP].chksum
        #send(pkt)

if __name__ == "__main__":
    print("Started packet capturing and dumping...Press CTRL+C to exit.")
    #sniff(prn=write_cap)
    #test_dumpfile()
    sniff(filter="tcp and ( port 80 )", prn=modify_packet_header)
    