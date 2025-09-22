DOCUMENTATION FOR ARP SPOOFER:

MAIN COMPONENTS USED IN THIS PROJECT ARE:
 
*MODULES:
. scapy: . As we already discussed that it is a module through which we can easily sniff, sent or receive packets on a local area network.
         . In this project the main concept is used is ARP (Address Resolution Protocol).

. time: . This module is new for us and mainly used to introduce delay in our program.
        . In our project we used this module so that the flooding of network with quick requests.

. sys: . This is generaly used to terminate the program or interrupt the program.
       . In our project we use CTRL+C to terminate the loop or we can say that stop the forwarding of packets to the target machine.


*NEW CONCEPTS APPLIED ARE:
. try and except statements: . These are generally used in exception handling.
                             . In our program we have used the try block to send multiple packets to the target machine.
                             . Except is used in our program to replace the dirty code when we press CTRL+C with printing something which provide some addtional
                               information.                                                                                             

. echo 1 > /proc/sys/net/ipv4/ip_forward: . This a new and very useful statement for us because when we are running are python script we are able to spoof the target                      
                                            machine but the main issue is that the target machine will not be able to browse internet and the main reason behing this is 
                                            that the packets are not forwarded to the target machine.
                                          . So now this command comes into play which allow us to forward the packet to the target machine so that they can browse the
                                            internet without any interruption.
                               
*SOME IMPORTANT TERMS:
. pdst stands for packet destination as the name suggested the IP address of target machine is given in this part.
. dst stands for destination in which the destination mac address is set to broadcast mac.
. hwdst stands for hardware destination address in which we provide the mac address of the target's machine.
. psrc stands for packet source address and in this we provide the ip of the router.
. hwsrc stands for hardware source address in which we provide the mac address of the router.


*MAIN METHODOLOGY:
. So in our program the main thing is that we are saying to the target machine that we are the router and you can access all the services from us.
. Secondly we tell the router that we are the target machine you are providing the services to us only.
. But the reality is that with this process we became the Man In The Middle by which all the services provided by the router or all the request sent by the target's 
  machine is flowing via our machine and with this we have succesfully spoofed the arp.

*CONFUSING POINT:
 
*WHOSE IP ADDRESS AND MAC ADDRESS ARE PASSED WHEN AND HOW?
. In this question the problem is that we can be confused that if we want to become the Man In The Middle then our IP and MAC should be used ?
  But no this is not the correct way.
. Actually we firstly fool the target's machine by providing them the routers IP address and MAC and secondly we fool the router by providing them with the IP and MAC
  of the target machine.


*FINAL RESULT:
. So the final result is that when we fetch the IP and MAC of the target machine we see that the IP and MAC are of the router but after we execute our python script
  the changes we'll see is that the IP would be same as the router's IP but the MAC address will be changed to our kali machine's MAC, So the packets will flow through 
  our machine.
