#!/usr/bin/env/ python
from ipaddress import ip_address

import scapy.all as scapy # In this we have used ARP protocol which stands for address request protocol
# import optparse
import argparse

def arguments():
    # parser=optparse.OptionParser()
    parser=argparse.ArgumentParser()
    # parser.add_option("--ip","--i", dest="ip_address", help="Enter the IP to scan the network")
    parser.add_argument("--ip","--i", dest="ip_address", help="Enter the IP to scan the network")
    option=parser.parse_args()
    if not option.ip_address:
        print("Please enter a valid MAc address or type --help for more information")
    return option

def scan(ip_address):
    arp_request=scapy.ARP(pdst=ip_address)
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #set the destination mac to broadcast mac
    arp_request_brodcast=broadcast/arp_request
    answered_list = scapy.srp(arp_request_brodcast, timeout=1, verbose=False)[0]

    client_list=[]


    for element in answered_list:
        client_dict={"ip":element[1].psrc, "mac":element[1].hwsrc}
        client_list.append(client_dict)
    return client_list

def print_result(result_list):
    print("IP\t\t\tMAC Address\n-------------------------------------------------")
    for client in result_list:
        print(client["ip"]+"\t\t"+client["mac"])

option=arguments()
scan_result=scan(option.ip_address)
print_result(scan_result)



