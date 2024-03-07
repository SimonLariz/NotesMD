## Wireshark Lab 3: DNS

1. Run nslookup to obtain the IP address of a Web server in Asia. What is the IP address of that server? 
nslookup nicovideo.jp

2. Run nslookup to determine the authoritative DNS servers for a university in Europe.
nslookup cam.ac.uk 

3. Run nslookup so that one of the DNS servers obtained in Question 2 is queried for the mail servers for Yahoo! mail.
nslookup cam.ac.uk mail.yahoo.com 

4. Locate the DNS query and response messages. Are they sent over UDP or TCP?
The DNS query and response messages are sent over UDP.

5. What is the destination port for the DNS query message? What is the source port of DNS response message?
The destination port for the DNS query message is 53. The source port of the DNS response message is 42105.

6. To what IP address is the DNS query message sent? Use ipconfig to determine the IP address of your local DNS server. Are these two IP addresses the same?
The DNS query message is sent to 192.168.1.1 which is the IP address of my local DNS server.

7. Examine the DNS query message. What “Type” of DNS query is it? Does the query message contain any “answers”?
Yes, the query message contains an answer. The type of DNS query is A.

8. Examine the DNS response message. How many “answers” are provided? What does each answer contain?
There are several answers provided, some include ipv4 addresses and some include ipv6 addresses (Both A and AAAA records).

9. Consider the subsequent TCP SYN packet sent by your host. Does the destination IP address of the SYN packet correspond to any of the IP addresses provided in the DNS response message?
Yes, the destination IP address of the SYN packet corresponds to one of the IP addresses provided in the DNS response message.

10. This webpage contains images. Before retrieving each image, does your host issue new DNS queries?
No, the host does not issue new DNS queries before retrieving each image.

11. What is the destination port fot the DNS query message? What is the source port of the DNS response message?
The destination port for the DNS query message is 53. The source port of the query message is 60779.

12. To what IP address is the DNS query message sent? Use ipconfig to determine the IP address of your local DNS server. Are these two IP addresses the same?
The DNS query message is sent to 192.168.1.1 which is the IP address of my local DNS server.

13. Examine the DNS query message. What “Type” of DNS query is it? Does the query message contain any “answers”?
There are 2 DNS queries, one for A and one for AAAA. The query message does not contain any answers.

14. Examine the DNS response message. How many “answers” are provided? What does each answer contain?
There are 2 answers provided, one for A and one for AAAA. Each answer contains an IP addresses.

15. Provide a screenshot

16. To what IP address is the DNS query message sent? Is this the IP address of your default local DNS server?
The DNS query message is sent to 192.168.1.1 which is the IP address of my local DNS server.

17. Examine the DNS query message. What “Type” of DNS query is it? Does the query message contain any “answers”?
The type of DNS query is NS. The query message does not contain any answers.

18. Examine the DNS response message What MIT nameservers does the response message provide? Does this response message also provide the IP addresses of the MIT nameservers?
The response message provides the names of the MIT nameservers. The response message also provides additional records which are of type A.

19. Provide a screenshot
See above

20. To what IP address is the DNS query message sent? Is this the IP address of your default local DNS server? If not, what does the IP address correspond to?
The system sends two DNS query messages to 192.168.1.1 which is the IP address of my local DNS server. One query is for A and the other is for AAAA. The next 2 queries are sent to 18.0.72.3 which is the IP address which my local DNS server resolved to. After that the two queries are sent to 18.0.72.3 before they time out.

21. Examine the DNS query message. What “Type” of DNS query is it? Does the query message contain any “answers”?
There are two DNS queries, one for A and one for AAAA. The query message does not contain any answers.

22. Examine the DNS response message. How many “answers” are provided? What does each answer contain?
There are 2 answers provided, one for A and one for AAAA. The first set of answers are from the local DNS server and the second set of query never receives a response from the DNS server.

23. Provide a screenshot
See above