## Week 2 

# TCP Model
TCP Model - a model of the internet that has 4 layers: application, transport, network, and network interface

# Internet
Internet - a "network of networks", interconnected ISPs, which are interconnected networks of computers

The internet is an infrastructure that allows for the exchange of data between computers

# Protocols
Protocols - a set of rules that govern the communication between computers, EX: TCP, IP, HTTP, FTP, SMTP, etc.

# Network Terminology
* Host - a computer connected to a network
* Router - a device that forwards data packets between computer networks
* Switch - a device that connects devices together on a computer network

* Network edge - the part of the network where hosts reside
* Network core - the part of the network where routers reside

* Client - a computer that requests data from a server
* Server - a computer that provides data to a client

* Transmission Rate - the speed at which data is transmitted, measured in bits per second (bps)

# Network Access 
Cable-based access - uses a cable to connect to the internet, EX: DSL, Fiber, etc.
* Multiplex

# Host: sends packets of data
Checksum in transport layer - a value that is used to check the integrity of data, pretty accurate but not 100% accurate

One's Compliment - reverse the bits of a number
* 1's Compliment of 1101 = 0010

Two's Compliment - reverse the bits of a number and add 1
* 2's Compliment of 1101 = 0011

Application  - Message
Transport - Segment
Network - Datagram
Data Link - Frame
Physical - Packet

# Physical Link
Bit - propagates between transmitter and receiver

Physical Link - lies between transmitter and receiver

Guided Media - signals propagate in solid media, EX: copper, fiber, etc.

Unguided Media - signals propagate freely, EX: radio, microwave, etc.

Twisted Pair - two insulated copper wires, twisted together, used for telephone lines
* Cat 5 - 100 Mbps, 1 Gbps Ethernet
* Cat 6 - 10 Gbps 

Coaxial Cable - a copper wire surrounded by insulation and a braided shield, bidirectional, 100 Mbps per channel

Fiber Optic Cable - a glass or plastic fiber that carries light, high bandwidth, long distance, immune to electromagnetic interference, 10s-100s Gbps, low error rate

Wireless Radio - uses radio waves to transmit data, 1 Mbps - 1 Gbps, 2.4 GHz, 5 GHz, no physical link, susceptible to interference

Radio Link Types:
* Terrestrial Microwave - up to 45 Mbps channels
* Wireless LAN (WiFi) - up to 100 Mbps
* Wide Area Network (cellular) - 3G, 4G, 5G
* Satellite - 45 Mbps per channel, high latency

Simplex - one direction
Half-duplex - both directions, but not at the same time
Full-duplex - both directions at the same time

# Network Core
Network Core - mesh of interconnected routers

Packet Switching - host breaks application layer messages into packets, packets are transmitted to the network core, packets are routed to the destination, packets are reassembled into the application layer message..

# Packet Switching: store and forward
Store and Forward - the entire packet must arrive at the router before it can be transmitted to the next router

Transmission Delay - the time it takes to push the packet into the link

# Packet Switching: Queuing Delay
Packet queuing and loss - if arrival rate (in bps) to link exceeds transmission rate, packets will queue, if the queue is full, packets will be dropped