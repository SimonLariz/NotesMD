## Wireshark 5

# 1. Select one UDP packet from your trace. From this packet, determine how many fields there are in the UDP header. Name these fields.
There are four fields in the UDP header. The fields are Source Port, Destination Port, Length, and Checksum.

# 2. By consulting the displayed information in Wireshark's packet content field for this packet, determine the length (in bytes) of each of the UDP header fields.
The length of the Source Port field is 2 bytes, the length of the Destination Port field is 2 bytes, the length of the Length field is 2 bytes, and the length of the Checksum field is 2 bytes.

# 3. The value in the Length field is the length of what? (You can consult the text for this answer.) Verify your claim with your captured UDP packet.
The value of the length field is the length of the UDP header and the UDP data. So header + payload. The length of the UDP header is 8 bytes, and the length of the UDP data is 127 bytes. The total length of the UDP packet is 135 bytes.

# 4. What is the maximum number of bytes that can be included in a UDP payload? (Hint: the answer to this question can be determined by your answer to question 2 above.)
The maximum number of bytes that can be included in a UDP payload is 65527 bytes. Which is 2^16 - 1 - 8 = 65527 bytes.

# 5. What is the largest possible source port number?
The largest possible source port number is 65,535 (2^16 - 1).

# 6. What is the protocol number for UDP? Give your answer in both hexadecimal and decimal notation. To answer this question, you'll need to look in the Protocol field of the IP datagram containing your UDP segment.
The protocol number for UDP is 17 in decimal and 0x11 in hexadecimal.

# 7. Examine a pair of UDP packets in which your host sends the first UDP packet and the second UDP packet is a reply to this first UDP packet. Describe the relationship between the port numbers in the two packets.
The port numbers are swapped in the two packets. The source port number in the first packet is the destination port number in the second packet, and the destination port number in the first packet is the source port number in the second packet.