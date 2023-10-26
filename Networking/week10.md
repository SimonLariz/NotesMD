## Week 10

Packet Filtering Firewall - A firewall that filters packets based on the contents of the packet header. It can be used to block packets from certain IP addresses or ports.

When no rules apply to a packet, default rule is applied
- Default deny - deny all packets unless explicitly allowed
- Default forward - forward all packets unless explicitly denied

Ports 0 - 1024: Ephemeral ports - used by the OS for communication between processes
Ports 0 - 1023 : Common ports - used by common services

Before TCP connection, a SYN packet is sent to the server. The server responds with a SYN-ACK packet. The client then responds with an ACK packet. This is called the TCP 3-way handshake.

iptables - Linux firewall, supports packet filtering, NAT, and port forwarding

Stateful firewall - A firewall that keeps track of the state of a connection. It can be used to block packets that are not part of an established connection.

Application-Level Gateway - A firewall that acts as a proxy for a specific application. It can be used to block packets that do not conform to the application protocol.

Virtual Firewall - A firewall that is implemented in software. It can be used to block packets that are not part of an established connection.

Hardware Firewall - A firewall that is implemented in hardware. It can be used to block packets that are not part of an established connection.