## Chapter 3 HW
## Problems: R1, R2, R5, R14, P1, P2 

## R.1 Suppose the network layer provides the following service. The network layer in the source host accepts a segment of maximum size 1,200 bytes and a destination host address from the transport layer. The network layer then guarantees to deliver the segment to the transport layer at the destination host. Suppose many network application processes are running at the destination host.
a. Design the simplest possible transport-layer protocol that will get application data to the desired process at the destination host. Assume the operating system in the destination host has assigned a 4-byte port number to each running application process. 

The simplest transport-layer protocol which will meet the requirements is a protocol which uses 4 bytes of the 1200 byte segment to store the port number of the destination host. The remaining 1196 bytes will be used to store the application data. The source host will send the segment to the destination host, which will then extract the port number from the segment and deliver the application data to the appropriate process.

b. Modify this protocol so that it provides a "return address" to the destination process.

The protocol can be modified by adding an additional 4 bytes to the segment to store the return address. The source host will send the segment to the destination host, which will extract the port number and return address from the segment. The destination host will then use the return address to send a response back to the source host. An example segment would be as follows: 4 bytes for the port number, 4 bytes for the return address, and 1192 bytes for the application data.

c. In your protocols, does the transport layer "have to do anything" in the core of the computer network?

No, since our protocol is designed to deliver application data to the desired process at the destination host, the transport layer does not have to do anything in the core of the computer network. The transport layer only needs to ensure that the segment is delivered to the destination host, where the application data can be extracted and delivered to the appropriate process.

## R.2 Consider a planet where everyone belongs to a family of six, every family lives in its own house, each house has a unique address, and each person in a given house has a unique name. Suppose this planet has a mail service that delivers letter from source house to destination house. The mail service requires that (1) the letter be in an envelope, and that (2) the address of the destination house (and nothing more) be clearly written on the envelope. Suppose each family has a delegate family member who collects and distributes letters for the other family members. the letters do not necessarily provide any indiction of the recipients of the letters.
a. Using the solution to Problem R1 above as inspiration, design a protocol that that the delegates can use to deliver the letters to the correct recipient.

Using the solution to Problem R1 as inspiration, a protocol which can be adopted would force the letter to contain the recipient's name along side the contents of the letter. The delegate would then deliver the letter to the correct recipient based on the name written on the letter.

b. In your protocol, does the mail service ever need to open the envelope and examine the contents of the letter?

No, the mail service does not need to open the envelope and examine the contents of the letter. The address of the destination house is clearly written on the envelope, and the delegate family member can deliver the letter to the correct recipient based on the name written on the letter.

## R.5 Why is it that voice and video traffic is often sent over TCP rather than UDP in today's Internet? (Hint: The answer we are looking for has nothing to do with TCP's congestion-control mechanism.)
Voice and video traffic are often sent over TCP rather than UDP in today's internet as it provides guaranteed in-order delivery of packets. Unlike TCP, UDP prioritizes speed over reliability, which can result in lost or out-of-order packets. 

## R.14 True or false?
a. Host A is Sending Host B a large file over a TCP connection. Assume Host B has no data to send Host A. Host B will not send acknowledgements to Host A because Host B cannot piggyback the acknowledgements on data.

False. Host B can send acknowledgements to Host A even if it has no data to send. Host B can piggyback the acknowledgements on the next data segment it sends to Host A.

b. The size of the TCP rwnd never changes throughout the duration of the connection.

False. The size of the TCP rwnd can change throughout the duration of the connection based on the available buffer space at the receiver.

c. Suppose Host A is sending Host B a large file over a TCP connection. The number of unacknowledged bytes that A sends cannot exceed the size of the receive buffer.

True. The number of unacknowledged bytes that A sends cannot exceed the size of the receive buffer at B.

d. Suppose Host A is sending Host B a large file over a TCP connection. If the sequence number for a segment of the file is m, then the sequence number for the subsequent segment of the file must be m+1.

False. The sequence number for the subsequent segment of the file does not have to be m+1. The sequence number can be any value as long as it is within the valid range.

e. The TCP segment has a field in its header for rwnd.

True. The TCP segment has a field in its header for rwnd, which indicates the size of the receive window.

f. Suppose that the last SampleRTT in a TCP connection is equal to 1 sec. The current value of TimeoutInterval is 1 sec and the current value of EstimatedRTT is 1 sec. The next EstimatedRTT will be >= 1 sec.

False. The next EstimatedRTT will be less than 1 sec

g. Suppose Host A sends one segment with sequence number 38 and 4 bytes of data over a TCP connection to Host B. In this same segment the acknowledgment number is 42.

True. 

## P.1 Suppose Client A initiates a Telnet session with Server S. At about the same time, Client B also imitates a Telnet session with Server S. Provide possible source and destination port numbers for:
a. The segments sent from A to S
    Source Port: Random ephemeral port number assigned by the operating system, Destination Port: 23 (Telnet)
b. The segments sent from B to S
    Source Port: Random ephemeral port number assigned by the operating system, Destination Port: 23 (Telnet)
c. The segments sent from S to A
    Source Port: 23 (Telnet), Destination Port: Random ephemeral port number assigned by the operating system
d. The segments sent from S to B
    Source Port: 23 (Telnet), Destination Port: Random ephemeral port number assigned by the operating system
e. If A and B are different hosts, is it possible that the source port number in the segments from A to S is the same as the source port number in the segments from B to S?
    Yes, it is possible for the source port number in the segments from A to S to be the same as the source port number in the segments from B to S if the operating system assigns the same port number to both clients. The IP address of the source host will be different, so the segments can be distinguished based on the IP address.
f. How about if they are the same host?
    If A and B are the same host, the source port number in the segments from A to S cannot be the same as the source port number in the segments from B to S. The operating system will assign different port numbers to each client, even if they are running on the same host.

## P.2 Consider Figure 3.5. What are the source and destination port values in the segments flowing from the server back to the clients? What are the IP addresses in the network-layer datagrams carrying the transport-layer segments?

Segment From Server to Client A:
    Source: 80, Destination: 26145

Segment From Server to Client B:
    Source: 80, Destination: 7532
