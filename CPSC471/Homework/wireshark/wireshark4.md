## Wireshark Lab 4

### 1. What is the IP address and TCP port number used by the client computer (source) that is transferring the file to gaia.cs.umass.edu? To answer this question, it is probably easiest to select an HTTP message and explore the details of the TCP packet used to carry this HTTP message, using the “details of the selected packet header window”.

IP Address: 10.0.2.15 
TCP Port: 33898

### 2. What is the IP address of gaia.cs.umass.edu? On what port number is it sending and receiving TCP segments for this connection?

IP Address: 128.119.245.12
Port: 80

### 3. What is the IP address and TCP port number used by your client computer (source) to transfer the file to gaia.cs.umass.edu?

IP Address: 10.0.2.15 
TCP Port: 33898

### 4. What is the sequence number of the TCP SYN segment that is used to initiate the TCP connection between the client computer and gaia.cs.umass.edu? What is it in the segment that identifies the segment as a SYN segment?
The sequence number of the SYN segment is 0. The SYN flag is set to 1 in the TCP header.

### 5. What is the sequence number of the SYNACK segment sent by gaia.cs.umass.edu to the client computer in reply to the SYN? What is the value of the Acknowledgement field in the SYNACK segment? How did gaia.cs.umass.edu determine that value? What is it in the segment that identifies the segment as a SYNACK segment?
The sequence number of the SYNACK segment is 0. The Acknowledgement field is 1. The server determined the value of the Acknowledgement field by adding 1 to the sequence number of the SYN segment. The SYN and ACK flags are set to 1 in the TCP header.


### 6. What is the sequence number of the TCP segment containing the HTTP POST command? Note that in order to find the POST command, you’ll need to dig into the packet content field at the bottom of the Wireshark window, looking for a segment that has “POST” within its DATA field.
The sequence number of the TCP segment containing the HTTP POST command is 1.

### 7. Consider the TCP segment containing the HTTP POST as the first segment in the TCP connection. What are the sequence numbers of the first six segments in the TCP connection (including the segment containing the HTTP POST)? At what time was each segment sent? When was the ACK for each segment received? Given the difference between when each TCP segment was sent, and when its acknowledgement was received, what is the RTT value for each of the six segments? What is the EstimatedRTT value (see Section 3.5.3, page 242 in text) after the receipt of each ACK? Assume that the value of the EstimatedRTT is equal to the measured RTT for the first segment, and then is computed using the EstimatedRTT equation on page 242 for all subsequent segments.
The first six segments in the TCP connection are: #4,5,6,7,12,16, The sequence numbers are 1, 2921, 5841, 8761, 11681, 14601.

Segment 1: 0.083384284	
Segment 2: 0.083402633	
Segment 3: 0.083442513	
Segment 4: 0.083455219
Segment 5: 0.083529277	
Segment 6: 0.083527996	



### 8. What is the length of each of the first six TCP segments?
Segment 1: 2920 bytes
Segment 2: 2920 bytes
Segment 3: 2920 bytes
Segment 4: 2920 bytes
Segment 5: 2920 bytes
Segment 6: 11680 bytes

### 9. What is the minimum amount of available buffer space advertised at the received for the entire trace? Does the lack of receiver buffer space ever throttle the sender?
The minimum amount of available buffer space advertised at the receiver for the entire trace is 65535 bytes. The lack of receiver buffer space never throttles the sender.

### 10. Are there any retransmitted segments in the trace file? What did you check for (in the trace) in order to answer this question?
There are no retransmitted segments in the trace file. I checked for segments with the same sequence number. 

### 11. How much data does the receiver typically acknowledge in an ACK? Can you identify cases where the receiver is ACKing every other received segment (see Table 3.2 on page 283 in the text).
Receiver typically acknowledges 1460 bytes in an ACK. The receiver ACKs every other received segment when the receiver advertises a window size of 2920 bytes.

### 12. What is the throughput (bytes transferred per unit time) for the TCP connection? Explain how you calculated this value.
The throughput for the TCP connection is 1.2 MB/s. I calculated this value by dividing the total number of bytes transferred by the total time taken to transfer the file.

## 13. Use the Time-Sequence-Graph(Stevens) plotting tool to view the sequence number versus time plot of segments being sent from the client to the gaia.cs.umass.edu server. Can you identify where TCP’s slowstart phase begins and ends, and where congestion avoidance takes over? Comment on ways in which the measured data differs from the idealized behavior of TCP that we’ve studied in the text.
The slow start phase begins at the start of the connection and ends at the final segment. The congestion avoidance phase takes over after the slow start phase. The measured data differs from the idealized behavior of TCP in that the throughput is not constant and the congestion avoidance phase is not as smooth as the idealized behavior.

### 14. Answer each of two questions above for the trace that you have gathered when you transferred a file from your computer to gaia.cs.umass.edu
