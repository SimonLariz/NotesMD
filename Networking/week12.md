IP Sec is a collection of various portocols 
- Authentication Header (AH)
- Encapsulating Security Payload (ESP)

AH mode is useful when encryption is not needed or not allowed, but authentication is required. ESP mode is useful when encryption is required.

IPSec Transport Mode - only the payload of the IP packet is encrypted and/or authenticated. The IP header is not encrypted or authenticated. This mode is used for host-to-host communication, Can be transparent to end systems 

IPSec Tunnel Mode - the entire IP packet is encrypted and/or authenticated. This mode is used for network-to-network communication.
End routers are IPsec aware. Hosts are not.
    - Entire packet is encapsulated in a new IP header that specifies the tunnel endpoints (source and destination).

Security association (SA) - a simplex "connection" that affords security services to the traffic carried by it. 
    - SA is uniquely identified by a triple: Security Parameter Index (SPI), Destination IP address, Security Protocol Identifier (AH or ESP)
    - SA is unidirectional. Two SAs are required for bidirectional communication.
    - SA is negotiated between two IPsec peers using the Internet Key Exchange (IKE) protocol.


How R1 converts original datagram into IPsec datagram
- ESP header:
    SPI is a 32 bit number that uniquely identifies the SA, The receiver uses SPI to select the SA to use for processing the packet, Sequence number is used to prevent replay attacks

Algorithm at Receiver
- Receiver uses SPI to select the SA to use for processing the packet
- Sliding window of size W is used to prevent replay attacks

Internet Key Exchange (IKE) - used to negotiate the SA between two IPsec peers. IKE is a hybrid protocol that uses public key cryptography to authenticate the peers and to generate a shared secret key. The shared secret key is then used to generate the symmetric keys used by AH and ESP.
    - Phase 1: IKE SA negotiation
    - Phase 2: IPsec SA negotiation

    Share with preshared key or public key cryptography (RSA)


## Penetration Testing
Penetration Testing - Legal and authorized attempt to locate and exploit vulnerable systems for the purpose of making those systems more secure.

Scope and Rules of Engagement - contract between the penetration tester and the client. It defines the scope of the penetration test and the rules of engagement. It is a legal document that protects both parties. It is signed by both parties before the penetration test begins.

Red Team - the penetration tester

Blue Team - the defenders

