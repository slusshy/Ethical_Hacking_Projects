DOCUMENTATION FOR NETWORK SCANNER

MAIN PURPOSE OF THIS PROJECT:
. To scan any network and in return we will get the number of devices connected to that network along with their mac addresses.

COMPONENTS USED IN THIS PROJECT:
. We have used scapy module which include the main thing which is ARP(Address Resolution Protocol).

*What is ARP:
. It is a inter changing process that connects the virtual address that is IP address to the physical address which is mac address in a local area network(LAN).
. In this is mapping procedure the translation is very important as the most used IP address is IPV4 which is of 32 bits and MAC address is of 48 bits so ARP translates  
  accordingly.

*What actually ARP do and how it does it ?
. So basically ARP says hello IP address to a local area network and the devices that are connected to that local area network. Now what ARP does is scan all the ports 
  and gives back the device which has the same IP address along with the mac address.
. So we have successfully scanned a local area network and got all the devices along with their MAC addresses.

*What is scapy module?
. scapy is a python module which can sniff, send, dissect and forge network packets.

*Other modules used in this project are:
.optparse
