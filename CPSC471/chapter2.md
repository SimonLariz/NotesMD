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

# Web and HTTP
- Web page consists of objects, each of which can be stored on different servers
- Objects can be HTML file, JPEG image, Java applet, audio clip, etc.
- Web page consist of base HTML file which includes several referenced objects

# HTTP connections 
- Persistent HTTP
* TCP connection is opened
* Multiple objects can be sent over single TCP connection between client and server
* TCP connection closed after all objects have been sent

- Non-persistent HTTP
* TCP connection opened
* One object sent over TCP connection
* TCP connection closed

# Non-Persistent HTTP
- Non-persistent HTTP requires 2 RTTs per object
- OS overhead for each TCP connection
- Browser opens multiple parallel TCP connections to fetch objects

# Persistent HTTP
- Persistent HTTP requires 1 RTT for all referenced objects
- OS overhead for each TCP connection

# HTTP Request Message
- GET
* Requests an object from server
* GET /somedir/page.html HTTP/1.1
* Host: www.someschool.edu
* User-agent: Mozilla/4.0

General format:
- Method, URL, version [REQUEST LINE]
- Headers [HEADER LINES]
- Blank line [CR LF]
- Optional message body [BODY]

#  Other HTTP Request Methods
- POST
* Submits data to be processed to server

- HEAD
* Asks server to leave requested object out of response

- PUT
* Uploads object to server

- DELETE
* Deletes object on server

# HTTP Status Codes
- 200 OK
* Request succeeded, requested object later in this message

- 301 Moved Permanently
* Requested object moved, new location specified later in this message

- 400 Bad Request
* Request message not understood by server

- 404 Not Found
* Requested document not found on this server

- 505 HTTP Version Not Supported
* HTTP protocol version not supported by server

# Maintaining user/server state: Cookies
- Cookies
* Server sends cookies to client, stored at client
* Cookies are included in subsequent HTTP requests from client to server
* Cookies can be used to implement user-authentication, shopping carts, recommendations, etc.

- Four Components of Cookies
* Cookie header line of HTTP response message
* Cookie header line in next HTTP request message
* Cookie file kept on user's host, managed by user's browser
* Back-end database at website

Example: 
- Susan uses browser to access Amazon
- Amazon server creates unique ID and sends it to Susan's browser (cookie)
- Susan's browser stores cookie
- When Susan returns to Amazon, browser sends cookie to Amazon
- Amazon uses cookie to look up Susan's user information

# Web Caches (Proxy Servers)
Goal: satisfy client request without involving origin server
- User configures browser to use web cache
- Browser sends all HTTP requests to web cache
- If object is in cache, web cache returns object
- If object is not in cache, web cache requests object from origin server, then returns object to client

Web Cache acts as both client and server, Cache typically installed by ISP, university, company

Web Cache benefits:
- Reduced response time for client request
- Reduced traffic on an institution's access link to the internet

# Conditional GET
- Goal: don't send object if client has up-to-date cached version
- Cache: specify date of cached copy in HTTP request
- Server: response contains no object if cached copy is up-to-date

# HTTP/2 
- Goal: reduce latency, improve network and server resource usage
- Increased flexibility at server in sending objects
- Transmission order of requested objects based on client-specific priority
- Divide objects into frames, schedule frames to mitigate head-of-line blocking

* HTTP 1.1, server responds in order of request (first come, first served)
* Head of line blocking - slow response to one request slows all other requests

## HTTP 3
- Goal: decreased delay in multi-object HTTP requests

HTTP3 adds security, per object error- and congestion- control over UDP

## Email
Three major components:
- User agents
- Mail servers
- Simple Mail Transfer Protocol (SMTP)

User Agent
- "Mail reader"
- Composing, editing, reading, and sending mail messages
- E.g. Outlook, Thunderbird, Apple Mail
- Outgoing, incoming messages stored on server

# Email Mail Servers
Mailbox - contains incoming messages for user
Messaging Queue - holds outgoing messages
SMTP protocol between mail servers to send email messages

# Mail Message Format
SMTP - Protocol for exchanging email between mail servers

- Header lines
* To: recipient
* From: sender
* Subject: what the message is about
* Body

# Mail Access Protocols
- Post Office Protocol (POP) (downloads messages to client)
- Internet Message Access Protocol (IMAP) (stores messages on server)
- HTTP (web-based email)

# DNS - Domain Name System
DNS is a distributed database implemented in hierarchy of many name servers, organized in zones, each responsible for a specific domain
- Application-layer protocol: hosts, name servers communicate to resolve names (address/name translation)

Example: 
![DNS Example](./img/chapter2/dns.gif)

# Top level domain (TLD) servers
- Responsible for com, org, net, edu, etc, and all top-level country domains (e.g. uk, fr, ca, jp)

# Authoritative DNS servers
- Organization's own DNS server, providing authoritative hostname to IP mappings for organization's named hosts

# Iterative query 
- Contacted server replies with name of server to contact
- "I don't know this name, but ask this server"

# Recursive query
- Puts burden of name resolution on contacted name server

# Caching, Updating Records
- Once (any) name server learns mapping, it caches mapping
- Cache entries timeout (disappear) after some time (TTL)
- TLD servers typically cached in local name servers

# DNS Records
- Type=A
    - Name is hostname
    - Value is IP address

- Type=NS
    - Name is domain (e.g. foo.com)
    - Value is hostname of authoritative name server for this domain

- Type=MX
    - Value is name of mail server associated with name
    
- Type=CNAME
    - Name is alias name for some "canonical" (the real) name
    - Value is canonical name

# DNS protocol messages
- Query and reply messages, both with same message format
- Message header
    - Identification
    - Flags
    - Number of entries in question, answer, authority, and additional sections

# Peer to Peer Applications
- No always-on server
- Arbitrary end systems directly communicate
- Peers are intermittently connected and change IP addresses
- Self scalability, no need for data centers

# Video Streaming and CDNs
- Stream video traffic: major consumer of internet bandwidth
- Challenge: scale up to millions of simultaneous users
- Challenge: heterogeneity (different users have different capabilities)
- Solution: Content Distribution Networks (CDNs)

Constant bit rate (CBR) - video encoded at fixed rate
Fixed bit rate (VBR) - video encoded at variable rate

Network delays are variable, so VBR is more challenging to deliver 

# Streaming multimedia: DASH
DASH - Dynamic Adaptive Streaming over HTTP
Server:
- Encodes video at multiple bit rates
- Stores multiple copies of video
- Each video segment is stored in multiple versions
- Each version is divided into segments
Client:
- Requests video segments from server
- Requests segments at different bit rates
- Monitors buffer fullness, network congestion
- Switches to different bit rate if necessary

Streaming Video = encoding + DASH + playout buffering 

# Content Distribution Networks
CDN - Content Distribution Network, a collection of web servers distributed across multiple locations to deliver content more efficiently to users