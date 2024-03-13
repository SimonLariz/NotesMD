# Chapter 3

## Transport Layer: Overview
- The transport layer is responsible for process-to-process communication.
- Understand principles behind transport layer services:
  - Multiplexing/demultiplexing
  - Reliable data transfer
  - Flow control
  - Congestion control

## Transport service and protocols
- Provide logical communication between application processes running on different hosts.
- Transport protocols run in end systems.
    - Senders: break application messages into segments, pass to network layer.
    - Receivers: reassemble segments into messages, pass to application layer.

## Transport vs network layer services and protocols
- Network layer: logical communication between hosts.
- Transport layer: logical communication between processes.

## Mutliplexing and demultiplexing
- Multiplexing: gather data from multiple sockets, add transport header, pass to network layer.
- Demultiplexing: data from network layer, deliver to correct socket.

## How Demultiplexing works
- Host receives IP datagrams.
    - Each datagram has source IP address, destination IP address.
    - Each datagram carries a transport-layer segment.
    - Each segment has a source port number, destination port number.
- Host uses IP addresses and port numbers to direct segment to appropriate socket.

## Connectionless transport: UDP
- No handshaking between UDP sender, receiver.
- Each UDP segment handled independently of others.
- Why is there no connection setup?
    - No connection state at sender, receiver.
    - Small header size.
    - No congestion control: UDP can blast away as fast as desired.

## Connection-oriented transport: TCP
- Before exchanging data, sender, receiver establish a connection.
- Handshaking (exchange of control messages) initializes sender, receiver state before data exchange.
- Why is there a connection setup?
    - Reliable data transfer.
    - Flow control.
    - Congestion control.

## Summary
- Multiplexing/demultiplexing: Based on segment, datagram header fields.
- UDP: demultiplexing based on destination port number (ONLY).
- TCP: demultiplexing based on all four header fields. (source IP, source port, destination IP, destination port)
- Multiplexing/demultiplexing: on all layers.

## Principles of reliable data transfer
- Reliable data transfer: important in many applications.
- Reliable data transfer: sender, receiver agree on sequence of data.
- Receiver: sends ACK when it receives data.
- Sender: retransmits data if it does not receive ACK.

## Reliable data transfer protocol (rdt)
RDT - reliable data transfer protocol, implemented in the transport layer.
- RDT1.0: no data loss, no bit errors.
- RDT2.0: channel with bit errors.
    - Underlying channel may flip bits in packet.
    - How to recover from errors?
        - Acknowledgements, receiver explicitly tells sender that packet was received correctly.
        - Retransmissions, sender retransmits packet if it does not receive an ACK.
    - Fatal Flaw: what if ACK/NAK corrupted?
- RDT2.1: channel with bit errors, no loss of data.
- RDT 3.0: channel with errors and loss
    - New channel assumption: underlying channel can lose packets.
        - checksum, sequence numbers, retransmissions will be of help but not enough.
    - Approach: sender waits a reasonable amount of time for an ACK.
        - If ACK not received, sender retransmits packet.
        - If packet is lost, sender will receive no ACK.
    - Pipelined protocols: sender can have up to N unacked packets in pipeline.

## Go-Back-N (GBN)
- Sender can send up to N frames without needing an ACK.
- Receiver only sends cumulative ACK.
- Sender has a timer for the oldest unacked packet.
- If timer expires, sender retransmits all unacked packets.

## Selective Repeat (SR)
- Receiver individually acknowledges all correctly received packets.
    - Buffers packets, as needed, for eventual in-order delivery to upper layer.
- Sender times out on individual packets for unacked packets.

## TCP: Overview
- Point-to-point: one sender, one receiver.
- Reliable, in-order byte stream: no message boundaries.
- Full duplex data: bi-directional data flow in same connection.
- Cumulative ACKs: receiver sends ACK for all bytes received.
- Pipelined: sender can send multiple packets before receiving ACK.
- Connection Oriented: handshaking (exchange of control messages) initializes sender, receiver state before data exchange.
- Flow control: sender will not overwhelm receiver.
- Receiver will handle out-of-order packets (Protocol does not describe how to handle out-of-order packets)

## TCP Segment Structure
- Source port, destination port: 16 bits each.
- Sequence number: 32 bits. (Counting bytes of data into the byte stream)
- Acknowledgement number: 32 bits. (Next byte expected by receiver)
- Header length: 4 bits. (Number of 32-bit words in header)
- Checksum: 16 bits. (Sum of header and data)
- TCP Options: variable length.
- Application data: variable length.

## TCP Sender (Simplified)
- Event: data received from application layer.
    - Create segment with sequence number.
    - Seq # is byte-stream number of first data byte in segment.
    - Start timer if not already running.

## TCP Flow Control
- Receiver controls sender, so sender does not overflow receiver's buffer by transmitting too much, too fast.
- TCP receiver advertises free buffer space by including rwnd value in TCP header of receiver-to-sender segments.

## TCP Connection Management
- Before exchanging data, sender, receiver establish a connection.
- Handshaking (exchange of control messages) initializes sender, receiver state before data exchange.
    - Agree on connection parameters.

## Closing TCP Connection
- Connection termination: each side closes its side of the connection.
- Send TCP segment with FIN bit = 1.

## Principles of congestion control
- Congestion: too many sources sending too much data too fast for network to handle.

    