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

