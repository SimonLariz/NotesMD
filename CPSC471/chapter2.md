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