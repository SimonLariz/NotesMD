## Final Exam Review Sheet

# IPv6 and NAT

1. Explain what NAT stands for and how it is used in networking. Give some examples of its practical applications and how to solve problems involving NAT.
    NAT - Network Address Translation, method of remapping one IP address space into another by modifying network address information in the IP header of packets while they are in transit across a traffic routing device. 

2. Discuss the pros and cons of NAT for network performance, securitym and scalability
    Pros - allows to extend the life of IPv4, allows to hide internal network structure, allows to use private IP addresses, allows to use one public IP address for multiple devices, Can add some overhead since packets are rewritten

    Cons - Limited to 60,000 connections (2 ^ 16), routers should only process packets up to layer 3, violates end-to-end principle, address shortage should instead be solved by IPv6

3. Compare and constrast the different techniques for NAT traversal. How do they work and when are they used?
    [TODO]

4. Describe the differences between the IPv4 and IPv6 protocols and their packet structures. What are the advantages and disadvantages of IPv6?
    IPv6 inital motivation: 32bit address space of IPv4 is not enough, IPv6 has 128bit address space

    IPv6 Removes: checksum, options, header length, fragmentation

5. Demonstrate your understanding of IPv6 tunneling by explaining how it works and why it is needed.
    Tunneling - IPv6 datagram carried as a payload in IPv4 datagram among IPv4 routers

    Tunneling is needed because IPv6 is not widely deployed, so IPv6 packets must be encapsulated in IPv4 packets to be sent across the internet

6. Be able to configure NAT in a Cisco router.

![Alt text](img/image.png)

R1 - Nat Router
    config t
    interface f1/0
    ip address dhcp
    no shutdown

    config t
    interface f0/0
    ip address 10.0.0.1 255.255.255.0
    no shutdown

    interface f1/0
    ip nat outside

    interface f0/0
    ip nat inside
    ip nat inside source list 1 interface f1/0 overload
    access-list 1 permit 10.0.0.0 0.0.0.255 
    ip route 0.0.0.0 0.0.0.0 192.168.122.1

Ubuntu Docker Guest
    Uncomment static ip 
    address: 10.0.0.3
    netmask: 255.255.255.0
    gateway: 10.0.0.1

    Now should be able to ping router gateway and nat cloud node


# Firewalling

1. What is a firewall?
    A firewall is a network security device that monitors incoming and outgoing network traffic and decides whether to allow or block specific traffic based on a defined set of security rules.

2. According to NIST SP 800-41, what are the characteristics of a firewall?
    1. IP Address Filtering: controls access based on IP address (e.g., source, destination, or both)
    2. Application Protocols: controls access based on application protocol data contained in the message (e.g., HTTP, FTP, Telnet, etc.)
    3. User Identification: controls access based on user identification (e.g., user name, password, etc.)
    4. Network Activity: controls access based on network activity characteristics (time of day, etc.)

3. What are the limitations of a firewall?
    Capabilties:
        - Define a traffic choke point in the network and protects against IP spoofing and routing attacks
        - Provide a location for monitoring the security events
        - Provide non-security functions: logging intenet usage, netwoork address translation, etc.
        - Serve as a platform for VPN/IPsec
    
    Limitations:
        - Cannot protect against attacks that bypass the firewall
        - Cannot protect against internal threats
        - Cannot protect against wireless connections between systems on the different sides of the firewall

4. What is a packet filter firewall? Be able to write and interpret rules and spot configuration flaws.
    Packet Filtering Firewall: applies a set of tules to each packet based on the packet headers

    Filter based on:
        - Source IP address
        - Destination IP address
        - IP Protocol 
        - Interface 

    When no rule matches, the default rule is applied
        - Default deny: drop the packet
        - Default allow: forward the packet

5. What is the difference between the default allow and default deny firewall policies? Which one is more secure?
    Default deny is more secure because it drops the packet when no rule matches

6. Be able to configure the packet filtering functions of iptables
    iptables --list: list all rules
    INPUT: incoming packets
    OUTPUT: outgoing packets
    FORWARD: packets that are neither incoming nor outgoing

    Example: Write iptables rules to block all ICMP traffic to and from the system
        iptables -A INPUT -p icmp -j DROP 
        iptables -A OUTPUT -p icmp -j DROP

    Example: Write iptables rules to block all traffic on port 22
        iptables -A OUTPUT -p tcp --dport 22 -j DROP
        iptables -A OUTPUT -p tcp --sport 22 -j DROP

    Exmaple: Write iptables rules to block traffic to host 192.168.2.2
        iptables -A OUTPUT -p tcp -d 192.168.2.2 -j DROP
        iptables -A OUTPUT -p tcp -s 192.168.2.2 -j DROP

7. What are the limitations of the packet filter firewall?
    Limitations:
        - Does not examine upper layer protocols (e.g., HTTP, FTP, etc.)
        - Cannot support advanced user authentication (inability to examine application data)
        - Can be fooled by IP address spoofing
        - Prone to misconfiguration (easy to make mistakes)
        - Source routing attacks (attacker can specify the route that the packet should take)
    
8. What is the stateful firewall and how does it compare to a packet filter?
    Stateful Firewall: can examine packets in the context of the connections of which they are a part of

    Stateful firewalls maintain a directory of inbound/outbound connections and can determine whether a packet is part of an existing connection (State table)

    Stateful firewalls can:
        - Block packets that do not match an existing connection
        - Block packets that match an existing connection but do not match the state of the connection
        - Allow packets that match an existing connection and match the state of the connection

9. What is the application-level firewall? What are its advantages and limitations?

10. What is a circuit-level firewall? Waht are its advantages and limitations?

11. What are the different approaches to basing the firewall?

12. What are the host-based firewalls?

13. What are the network device firewalls?

14. What are virtual firewalls?

15. What is the DMZ? How is it used for securing networks?

16. What are the advantages and disadvantages of having the two DMZ firewalls be from different vendors?

17. Be able to write pfSense firewall rules.