** DOCUMENTATION FOR PACKET SNIFFER USING PYTHON **

* MAIN CONCEPT:
. So previously we have built an ARP spoofer by which we can easily became the man in the middle that is we have spoofed the target machine using our machine.
. So every request is flowing through our computer.
. But the problem is that we are unable to capture or see the request or URLs or data used by the target machine, so now our packet sniffer comes into action.
. Using packet sniffer we can easily extract the required information like usernames, passwords, websites etc.

NOTE: Our packet sniffer can only capture the data on the extension http not https because https involves more complexity and it also adds more layers of protection.

* MODULES USED IN OUR PYTHON SCRIPT:
. scapy: .As we have already discussed it is mainly used to sniff, send and receive packets on a device connected to a network.

. from scapy we have imported http: . As it is imported/part of scapy module, So we can conclude that http is used to send or receive http packets only.
                                    . In our script we are trying to capture the activity of the target machine so http plays a very important role.

* MORE ABOUT scapy CONCEPTS:
. To sniff data we can simply write scapy.sniff().
. Now this sniff field accept many arguments but we have only used 3 which are iface, store, prn.
. iface as the name suggested used to specify the interface that is eth0 or lan0 etc.
. store allow us to whether we need to store the packets and we have set it to false to save memory and also they are not useful for us.
. prn is used to send the packets to the target's machine.

* EXTRACTION OF REQUIRED INFORMATION:
. Now we need to extract URLs and passwords so to do that we have used the http module.

* NEW CONCEPTS LEARNED IN THIS PROJECT:
. A new function which is decode() is used in our python script which is basically used for typecasting or we can say that alternative for str().
. To extract anything from the terminal we can use [http.HTTPRequest].name_of_the_field.
