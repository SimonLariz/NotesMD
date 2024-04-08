# Chapter 4: The Network Layer

## Network Layer: Goals
- Understand principles behind network layer services:
  - Logical communication between hosts.
  - Path determination.
  - Forwarding.
  - Routing.

- Instantiation, implementation in the Internet:
  - The Internet Protocol (IP)
  - NAT (Network Address Translation)

## Network Layer: Services and Protocols
- Transport segment from sending to receiving host.
    - Sender: encapsulates segments into datagrams.
    - Receiver: delivers segments to transport layer.

## NAT (Network Address Translation)
- Motivation: local network uses just one IP address as far as outside world is concerned:
  - Range of addresses not needed from ISP.
  - Can change addresses of devices in local network without notifying outside world.

- NAT translates private IP addresses to public IP addresses. 
- NAT knows where to send datagrams by keeping state information in NAT table.
- NAT Table: 
  - Each entry has fields for local IP address, local port number, global IP address, global port number.
  - When datagram received, NAT translates fields, replaces them with fields from NAT table.
  - NAT table entry is removed when connection closes.

## IPv6 Motivation
- Initial motivation: 32-bit address space completely allocated.
- Additional motivation:
  - Header format helps speed processing/forwarding.
  - Header changes to facilitate QoS.
  - Simplified processing by routers.

## Transition from IPv4 to IPv6
- Not all routers can be upgraded simultaneously.
- Tunneling: IPv6 datagram carried as payload in IPv4 datagram among IPv4 routers.

## Generalized Forwarding and SDN
- IP datagram remains unchanged as it travels through the network.
- Routers use forwarding table to determine where to send datagrams.

SDN (Software Defined Networking):
- Routers are dumb.
- SDN controller is smart.
- SDN controller tells routers where to send datagrams.

## OpenFlow: examples
- Routers can be programmed to:
  - Send certain packets to particular link.
  - Drop packets.
  - Send packets to specific controller.

## Middleboxes
- Middlebox is any intermediary device performing functions beyond simple forwarding.
- Ex: firewalls, NAT boxes, intrusion detection systems, WAN optimizers.

## End-to-End Argument
- Functionality should be placed in network core only if it cannot be implemented at edge.