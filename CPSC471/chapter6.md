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