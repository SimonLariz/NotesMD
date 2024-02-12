## Chapter 1 Review Questions:

# 1. What is the difference between a host and an end system? List several different types of end systems. Is a Web server an end system?

There is no difference between a host and an end system. They are terms which refer to the same thing. End systems are devices that are connected to a network and are capable of running applications. A web server is considered an end system.

Examples of end systems include:
- Desktops
- Laptops
- Mobile devices
- Servers
- Routers

# 2. The word protocol is often used to describe diplomatic relations. How does Wikipedia describe diplomatic protocols?

Wikipedia describes diplomatic protocols as "the etiquette of diplomacy and affairs of state. It may also refer to an international agreement that supplements or amends a treaty." [Wikipedia](https://en.wikipedia.org/wiki/Protocol_(diplomacy))

# 3 Why are standards important for protocols?

Standards are important for protocols because they ensure that devices from various manufactures can all communicate with each other. Without standards, the protocols used by different devices would be incompatible and unable to communicate.

# 4. List four access technologies. Classify each one as home access, enterprise access, or wide-area wireless access.

- DSL: Home access
- Ethernet: Enterprise access
- 4G: Wide-area wireless access
- Wi-Fi: Home access

# 8. What are some of the physical media that Ethernet can run over?

Ethernet can run over the following physical media:
- Twisted pair copper wire
- Coaxial cable
- Fiber optic cable

# 15. Some content providers have created their own networks. Describe Google's network. What motivates content providers to create these networks?

Google has created their own private network to connect their data centers. The use of a private networks allows Google to use the full bandwidth of the network and to avoid the congestion that can occur on the public internet. Content providers create their own networks to ensure that their content is delivered to users as quickly as possible.

# 24. What is an application-layer message? A transport-layer segment? A network-layer datagram? A link-layer frame?

Application-layer message - data which an application want to sent and which is sent to the transport layer for delivery to the destination application. EX: email, web page

Transport-layer segment - data which is sent from the application layer to the network layer. EX: TCP segment, UDP datagram

Network-layer datagram - data which is sent from the transport layer to the data link layer. EX: IP datagram

Link-layer frame - data which is sent from the network layer to the physical layer. EX: Ethernet frame

Consider an application that transmits data at a steady rate (for example, the sender generates an N-bit unit of data every k time units, where k is small and fixed). Also, when such an application starts, it will continue running for a relatively long period of time. Answer the following questions, briefly justifying your answer:

# P3a. Would a packet-switched network or circuit-switched network be more appropriate for this application? Why?

A circuit switched network would be more appropriate for this application. Circuit switched networks are more efficient for applications that transmit data at a steady rate. Once a circuit is established, the data can be transmitted without the overhead of setting up a connection for each packet. 

# P3b. Suppose that a packet-switched network is used and the only traffic in this network comes from such applications as described in (a). Furthermore, assume that the sum of the application data rates is less than the capacities of each and every link. Is some form of congestion control needed? Why?

Yes, some form of congestion control is needed. Even if the sum of the application data rates is less than the capacities of each and every link, congestion can still occur at other points in the network. Congestion control is needed to ensure that the network operates efficiently and that all applications receive a fair share of the network resources.

# P12. A packet switch receives a packet and determines the outbound link to which the packet should be forwarded. When the packet arrives, one other packet is halfway done being transmitted on this outbound link and four other packets are waiting to be transmitted. Packets are transmitted in order of arrival. Suppose that all packets are 1,500 bytes and the link rate is 2.5 Mbps. What is the queuing delay for the packet? More generally, what is the queuing delay when all packets have length L, the transmission rate is R, x bits of the packet have been transmitted, and n packets are already in the queue?

The queuing delay for the packet is the time it takes for the packet to be transmitted. Based on the information the packet length is 1500 bytes and the link rate is 2.5 Mbps. The current bits being transmitted is 750 bits since the packet is halfway done being transmitted and the number of packets in the queue is 4. The time to finish the current packet is (remaining bits) / (link rate) so the queuing delay is (750 bits) / (2.5 Mbps) ≈ 0.0012 seconds. The transmission of the packets in queue will be (number of packets) * (packet length) / (link rate) si the queuing delay is (4 packets) * (1500 bytes) / (2.5 Mbps) ≈ 0.0024 seconds. The total queuing delay is 0.0012 + 0.0024 ≈ 0.0036 seconds.
