** DOCUMENTATION FOR DNS SPOOFER **

* MAIN IDEOLOGY *
. So DNS stands for Domain Name System.
. In this project we have successfully modified the packets of a target machine using our ARP spoofing technique and DNS spoofing technique.


* MODULES USED IN OUR PYTHON SCRIPT *
. scapy: . As we already know from the previous projects it is basically used to send, sniff, record packets of a target machine using ARP .
. netfilterqueue: . It is used to receive, drop the packets using set of rules of an iptables.
                  . In our python script we used this module to modify the packets using our kali machine.
                  . Main idealogy in our python script is that when the target machine sends any kind of request to the router which will flow through our machine as we  
                    are man in the middle using arp_spoofer, so like the request will stored as a queue in our machine using which we can easily modify the packet and 
                    send it back to the target machine.

* FILTERING OF DATA AND USING IT TO MODIFY THE PACKET *
. So the packet is received but now the main objective is how we are going to modify it.
. Now the method to hold the packet to modify it is packet.payload().
. Now DNSRR stands for DNS Resource Record which basically see if a DNS request is made or not.
. Now DNSQR stands for DNS Question Record which is the original request made by the target.

* BASIC NEW METHODS LEARNED IN THIS PROJECT *
. To start our own web server provided by the kali is done by using a simple command which is :
  1. service apache2 start.

. To send a request to website using command prompt is done by:
  1. ping -c 1 web_page_name_along_with_extension .

. First of all in our script we need to use the iptables commands these are:
  1. iptables -I OUTPUT -j NFQUEUE --queue-num 0
  2. iptables -I INPUT -j NFQUEUE --queue-num 0

. After running this commands and finishing the attack we need to flush these iptables so that the internet continues without any disturbance.
  1. iptables --flush

*NOTE: The above iptables commands are for testing the attack on our personal machine.

. Now to run the attack on a virtual machine we need to run only command which is :
  1. iptables -I FORWARD -j NFQUEUE --queue-num 0
  2. iptables --flush (Again to reset the iptables).


* MAIN OUTPUT GENERATED *
. So in our attack we have become the man in the middle first in which the all the request sent by the target machine will flow through our machine. Then the second 
  step is that using our DNS spoofing technique we have modified the request.
. In our case the target has generated a request to a web page which www.vulnweb.com but we have directed the target to our web server which apache2.
