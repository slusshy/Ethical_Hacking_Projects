** DOCUMENTATION FOR FILE INTERCEPTING PYTHON SCRIPT **

* MAIN IDEALOGY *
. So basically in the last project we have successfully built an DNS spoofer using which we can easily redirect the user to some other we server or we 
  can redirect the target to some trojan containing sites.
. Now following the same method we have successfully built an file interceptor using which we can modify the downloads by becoming Man In The Middle and
  can pass any evil file or worm or any form of virus easily.


* MODULES USED *
. scapy : As we have used this multiple times in our previous projects it is a very powerful module using which we can send, receive or intercept the 
          the packets on a target machine connected to an network.

. netfilterqueue : We have also used this module in the previous project. This basically used to apply some set of rules of iptables.


* SPECIAL COMMANDS *
. echo 1 > /proc/sys/net/ipv4/ip_forward
. iptables -I INPUT -j NFQUEUE --queue-num 0------ NOTE : These two command are used when we are testing the attack on our own machine.
. iptables -I OUTPUT -j NFQUEUE --queue-num 0-------^
. iptables -I FORWARD -j NFQUEUE --queue-num 0-- NOTE : This command is used when we are performing the attack on the virtual or different machine.


* IMPORTANT FIELDS THROUGH WHICH WE HAVE FILTERED THE USEFULL DATA *
. In a packet we have two things the http request and the http response and both the fields have Raw layer in which we have the load layer in which we 
  see a particular keyword for the particular task. Like in our case we are trying to replace the download file so the keyword is GET.
. Since we are currently working on a http protocol so to filter useful data we need to remember the port name and in our case it is 80 for http.


* SOME IMPORTANT POINTS WITHOUT WHICH WE CANNOT RUN OUR PYTHON SCRIPT SUCCESSFULLY *
. As we know most of the websites are currently using the https protocol which we have not studied yet So, to test the attack we need a http web-site 
  and a download request which goes to a http web server and in our case we have used speedtest.tele2.net/ .
. Also since there are many downloadable files in the web servers so to intercept a particular download file we also have to select a particular file 
  like .exe , .PNG , .zip and in our case we have used a zip file.
