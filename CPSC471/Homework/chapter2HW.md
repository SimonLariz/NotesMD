## CPSC 471 Homework 2

### R1. List five nonproprietary Internet applications and the application-layer protocols that they use.

1. **Web** - HTTP
2. **Email** - SMTP, POP3, IMAP
3. **File Transfer** - FTP
4. **Remote Login** - SSH
5. **Remote Execution** - Telnet

### R5. What information is used by a process running on one host to identifdy a process running on another host?

The process running on one host uses the following information to identify a process running on another host:
- **IP Address** - The IP address of the host running the process.
- **Port Number** - The port number of the process running on the host.
Both the IP address and port number are used to identify the process running on another host.

### R6. Suppose you wanted to do a transaction from a remote client to a server as fast as possible. Would you use UDP or TCP? Why?

If speed is the main concern, then UDP would be the best choice. The UDP protocol is faster than TCP because it does not require a connection to be established before data is sent. This means that there is no need to wait for a connection to be established before data is sent. However, UDP does not guarantee that the data will be delivered to the destination, so it is not suitable for applications that require reliable data transfer.

### R9. Recall the RCP can be enhanced with TLS to provide process-to-process security services, including encryption. Does TLS operate at the transport layer or the application layer? If the application layer, then why?

TLS operates at the application layer as it provides security to the application layer. This is beneficial because it allows the application to be independent of the underlying network protocol. This means that the application can use any network protocol, such as TCP or UDP, and still be secure.

### R10. What is meant by a handshaking protocol?

A handshaking protocol is a protocol that establishes a connection between two devices. The handshaking protocol is used to negotiate the parameters of the connection and to ensure that both devices are ready to communicate.

### P1a. True or False: A user requests a Web page that consists of some text and three images. For this page, the client will send one request message and receive four response messages.

False. The client will send one request message and receive one response message. The response message will contain the text and the three images.

### P1b. True or False: Two distinct Web pages (for example, www.mit.edu/research.html and www.mit.edu/students.html) can be sent over the same persistent connection.

True. Two distinct Web pages can be sent over the same persistent connection. A persistent connection allows multiple requests and responses to be sent over the same connection.

### P1c. True or False: With nonpersistent connections between browser and origin server, it is possible for a single TCP segment to carry two distinct HTTP request messages.

False. With nonpersistent connections, each request message is sent in a separate TCP segment.

### P1d. True or False: The Date: header in the HTTP response message indicates when the object in the response was last modified.

False. The Date: header in the HTTP response message indicates the date and time at which the message was sent.

### P1e. True or False: HTTP response messages never have an empty message body.

False. HTTP response messages can have an empty message body.

### P3. Consider an HTTP client that wants to retrieve a Web document at a given URL. The IP address of the HTTP server is initially unknown. What transport and application-layer protocols besides HTTP are needed in this scenario?

In this scenario, the client will use the DNS protocol to resolve the IP address of the HTTP server. The DNS request will be sent using the UDP protocol. Once the IP address is resolved, the client will use the HTTP protocol to retrieve the Web document.