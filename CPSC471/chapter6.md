## Chapter 6 Link Layer

## Link Layer Introduction
Link layer has responsibility of transferring datagram from one nnode to physically adjacent node over a link
- Host and Routers: Node
- Communication channels that connect adjacent nodes along communication path: Link

## Link Layer: Services
Framing, Link acess:
- Encapsulate datagram into frame, adding header, trailer
- Channel access if shared medium
- "MAC" addresses used in frame headers to identify source, destination
Reliable delivery between adjacent nodes

Flow Control
- Pacing between adjacent sending and receiving nodes
Error Detection
- Errors caused by signal attenuation, noise
- Receiver detects presence of errors: signals sender for retransmission or drops frame
Error Correction
- Receiver identifies and corrects bit error(s) without resorting to retransmission
Half-duplex and full-duplex
- With half duplex, nodes at both ends of link can transmit, but not at same time
- With full duplex, nodes at both ends of link can transmit simultaneously

## Link Layer: Implementation
Link layer implemented in "adaptor" (aka network interface card)

## Cable access network
- DOCSIS: data over cable service interface specification
    - FDM over upstream and downstream frequency bands
    - TDM upstream

## MAC (Media Access Control) Addresses
32-bit IP address: network-layer address
MAC (or LAN or physical or Ethernet) address: used to get frame from one interface to another physically-connected interface (same network)

## ARP (Address Resolution Protocol)
ARP table: each IP node (host, router) on LAN has table
- IP/MAC address mappings for some LAN nodes
- TTL (Time To Live): time after which address mapping will be forgotten (typically 20 min)

## Routing to another subnet: addressing
Frame sent from one host to another, same LAN (same subnet)
- MAC address of destination
Frame sent from one host to another, different LAN (different subnet)
- MAC address of router interface
- Router's IP address in frame

## Summary of MAC protocols
- Channel Partitioning
    - Divide channel into smaller "pieces" (time slots, frequency, code)
    - Allocate piece to node for exclusive use
- Random Access
    - Channel not divided, allow collisions
    - "recover" from collisions
- Taking turns
    - Nodes take turns, but nodes with more to send can take longer turns

## MAC Addresses
- 32 bit IP address
    - network-layer address
- MAC (or LAN or physical or Ethernet) address
    - used to get frame from one interface to another physically-connected interface (same network)
    - 48 bit MAC address burned in NIC ROM
    - MAC address allocation administered by IEEE
        - Manufacturer buys portion of MAC address space (to assure uniqueness)
        - MAC address prefix (OUI) burned in NIC ROM

## ARP (Address Resolution Protocol) Table
Each IP node (host, router) on LAN has table
- IP/MAC address mappings for some LAN nodes

## ARP Protocol in action
- A wants to send datagram to B, and B's MAC address not in A's ARP table
- A broadcasts ARP query packet, containing B's IP address
- B receives ARP packet, replies to A with its (B's) MAC address
- A caches IP/MAC address pair in its ARP table until information becomes old (soft state)
- Soft state: information times out after some time (few minutes)
