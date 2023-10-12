## Week 8 

NAT - Network Address Translation

NAT Translation Table - A table that contains the mappings of inside local addresses to inside global addresses and outside local addresses to outside global addresses. (Replaces local addresses with global addresses)

No one can connect to a NAT system from the outside, without the NAT system first establishing a connection to the outside.

For each packet received the router can 
1. Drop the packet, if packet is expired
2. Deliver the packet to the destination host
3. Forward the packet to another router

How does a router know where to forward a packet? It uses a routing table based on AD (Administrative Distance) and metric.

# IP Spoofing

IP Spoofing is a technique used to gain unauthorized access to machines, whereby an attacker illicitly impersonates another machine by manipulating IP packets.

Sender changes the source address of the packet to an IP address for which it is authorized to communicate.
If the attacker sends an IP packet with a source address of a trusted host to a router that has no knowledge of the network topology, the router will forward the packet to the trusted host.


<!-- How can I IP Spoof -->
1. Find a trusted host
2. Find a router that has no knowledge of the network topology
3. Send a packet with the source address of the trusted host to the router
4. The router will forward the packet to the trusted host
5. The trusted host will send a reply to the spoofed address
6. The attacker will receive the reply
7 The attacker can now send packets to the trusted host using the spoofed address