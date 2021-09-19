from scapy.all import *
import sys

SYN = 0x02
ACK = 0x10
SYN_ACK = 0x12

SYN_packets = {}
SYN_ACK_packets = {}

num = 0

def main():
    with PcapReader(sys.argv[1]) as pr:
        for p in pr:
            if(p.haslayer(TCP)):
                msg = p['TCP'].flags
                if msg == SYN:
                    # print(p.show())
                    key = str(p['IP'].src) #create key
                    if key not in SYN_packets:          #if key is new
                        SYN_packets[key] = 1
                    else:                               #if key is already present
                        temp = SYN_packets.get(key)
                        temp += 1
                        SYN_packets[key] = temp
                elif msg == SYN_ACK:
                    key = str(p['IP'].dst) #create key
                    if key not in SYN_ACK_packets:      #if key is new
                        SYN_ACK_packets[key] = 1
                    else:                               #if key is already present
                        temp = SYN_ACK_packets.get(key)
                        temp += 1
                        SYN_ACK_packets[key] = temp

            # num += 1
            # if num % 1000000 == 0:
            #     break

    to_remove = []

    for key in SYN_packets:
        if key in SYN_ACK_packets:
            temp_syn = SYN_packets.get(key)
            temp_syn_ack = SYN_ACK_packets.get(key)
            if((temp_syn / temp_syn_ack) >= 3 ):
                print(str(key))
            to_remove.append(key)
        else:
            pass

    for key_remove in to_remove:
        SYN_packets.pop(key_remove)
        SYN_ACK_packets.pop(key_remove)

    for key in SYN_packets:
        print(key)

if __name__ == "__main__":
    main()