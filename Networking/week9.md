## Week 9 

IP Spoofing can be useful in DDOS attacks, where the attacker sends a packet with a spoofed source address to a router that has no knowledge of the network topology. The router will forward the packet to the spoofed address, which is the victim of the DDOS attack.

# IP Spoofing countermeasures

Ingress filtering - A technique used to ensure that incoming packets are actually from the source from which they claim to originate.
- blocks packets originating from outside the network that claim to originate from inside the network

Egress filtering - A technique used to ensure that outgoing packets are actually from the source from which they claim to originate.
- blocks packets originating from inside the network that claim to originate from outside the network