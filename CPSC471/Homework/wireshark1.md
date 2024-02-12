## Wireshark Lab 1 

# 1. List 3 different protocols that appear in the protocol column in the unfiltered packet-listing window in step 7.

- HTTP
- DNS
- TCP

# 2. How long did it take from when the HTTP GET message was sent until the HTTP OK reply was received?

It took about .083 seconds from when the HTTP GET message was sent until the HTTP OK reply was received.

# 3. What is the internet address of the gaia.cs.umass.edu (also known as www-net.cs.umass.edu)? What is the internet address of your computer?

The internet address of gaia.cs.umass.edu is 128.119.245.12 and the internet address of my computer is 172.16.32.130.

# 4. Print the two HTTP messages (GET and OK) that were sent by your computer. 

No.
Time
Source
Destination
Protocol Length Info
9 21:22:13.997883141 172.16.32.130
128.119.245.12
HTTP
436
GET /wireshark-
labs/INTRO-wireshark-file1.html HTTP/1.1
Frame 9: 436 bytes on wire (3488 bits), 436 bytes captured (3488 bits) on interface eth0, id 0
Ethernet II, Src: VMware_a2:86:cc (00:0c:29:a2:86:cc), Dst: VMware_e3:d9:0c (00:50:56:e3:d9:0c)
Internet Protocol Version 4, Src: 172.16.32.130, Dst: 128.119.245.12
Transmission Control Protocol, Src Port: 47534, Dst Port: 80, Seq: 1, Ack: 1, Len: 382
Hypertext Transfer Protocol


No.
Time
Source
Destination
Protocol Length Info
13 21:22:14.080451680 128.119.245.12
172.16.32.130
HTTP
492
HTTP/1.1 200
OK (text/html)
Frame 13: 492 bytes on wire (3936 bits), 492 bytes captured (3936 bits) on interface eth0, id 0
Ethernet II, Src: VMware_e3:d9:0c (00:50:56:e3:d9:0c), Dst: VMware_a2:86:cc (00:0c:29:a2:86:cc)
Internet Protocol Version 4, Src: 128.119.245.12, Dst: 172.16.32.130
Transmission Control Protocol, Src Port: 80, Dst Port: 47534, Seq: 1, Ack: 383, Len: 438
Hypertext Transfer Protocol
Line-based text data: text/html (3 lines)