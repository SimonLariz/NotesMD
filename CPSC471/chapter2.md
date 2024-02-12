## Chapter 2 

# TCP Model Review:
- TCP Model 
* Application
* Transport
* Network
* Data Link
* Physical

# Creating a network app
Write programs that
* Run on different end systems
* Communicate over a network
* Communicates with browser software

No need to write software for network core devices

# Client-Server Architecture
Client requests service, server provides service
Whoever initiates the communication is the client, the other is the server

Server
* Always-on host
* Permanent IP address
* Data centers for scaling

Client
* Communicates with server
* May be intermittently connected
* May have dynamic IP address
Example: HTTP, FTP, Telnet, Email

# Peer-to-Peer Architecture
* No always-on server
* Arbitrary end systems directly communicate
* Peers are intermittently connected and change IP addresses
* Self scalability, no need for data centers
Example: file sharing (torrents)

# Process Communication
Process - program running within a host
* Within same host, processes communicate using inter-process communication (IPC) defined by OS
* Processes in different hosts communicate by exchanging messages over the network

Client process initiates communication
Server process waits to be contacted

MTU - Maximum Transmission Unit - largest possible link layer frame

# Sockets
* Process sends/receives messages to/from its socket
* Sending process shoves message out door
* Sending process relies on transport infrastructure on other side of door to deliver message to socket at receiving process

# Addressing Processes
* To receive messages, process must have identifier
* Host device must have unique IP address

Identifier includes both IP address and port number

# Application-Layer Protocol Defines 
* Types of messages exchanged
- E.g. request, response

* Message syntax
- What fields in messages and how fields are delineated

* Message semantics
- Meaning of information in fields

* Rules for when and how processes send and respond to messages

* Open protocols
- Defined in RFCs, allowing for interoperability
- RFC - Request for Comments
- E.g. HTTP, SMTP

* Proprietary protocols
- E.g. Skype

# What Transport Services Does an App Need?
- Data integrity
* Some apps require 100% reliable data transfer (e.g. file transfer)
* Other apps can tolerate some loss (e.g. audio)

- Timing
* Some apps require low delay to be effective (e.g. internet telephony, games)

- Throughput
* Some apps require minimum amount of throughput to be effective (e.g. multimedia) 
* other apps make use of whatever throughput they get (e.g. email)

- Security
* Encryption, data integrity, etc.

# Transport Protocol Services
- TCP service
* Reliable transport between sending and receiving process
* Flow control - sender won't overwhelm receiver
* Congestion control - throttle sender when network overloaded
* Does not provide timing, minimum throughput guarantee, or security
* Connection-oriented - setup required between client and server processes

- UDP service
* Unreliable data transfer between sending and receiving process
* Does not provide flow control, congestion control, timing, throughput guarantee, or security