# Week 1 Topics

## CIA Triad with Examples
CIA - Confidentiality, Integrity, Availability
- Confidentiality: Only authorized users can access the data
    - Example: Encryption, access control
- Integrity: Data is accurate and reliable
    - Example: Hashing, checksums
- Availability: Data is available when needed
    - Example: Redundancy, backups

## Threat Actions, Consquences
- Unauthorized Disclosure: Loss of confidentiality, privacy
    - Exposure: Unauthorized access to data
    - Interception: Unauthorized access to data in transit
    - Inference: Unauthorized access to data by deducing from other data
    - Intrusion: Unauthorized access to data by bypassing security controls
- Deception: Loss of integrity
    - Masquerade: Unauthorized access to data by impersonating another entity
    - Falsification: Unauthorized modification of data
    - Repudiation: Unauthorized denial of data
- Disruption: Loss of availability
    - Incapacitation: Unauthorized denial of service
    - Corruption: Unauthorized modification of system resources
    - Obstruction: Unauthorized prevention of access to system resources
- Usurpation: Unauthorized control of system resources
    - Misappropriation: Unauthorized use of system resources
    - Misuse: Unauthorized use of system resources for unauthorized purposes

## Passive vs Active Attacks
- Passive: Eavesdropping, monitoring
    - Example: Sniffing, traffic analysis
- Active: Modification, destruction
    - Example: Injection, DoS

## Examples of Threats to Assets
- Hardware
    - Availability: Power failure, hardware failure
    - Confidentiality: Theft, tampering

- Software
    - Integrity: Unauthorized modification, deletion
    - Availability: Software failure, bugs
    - Confidentiality: Unauthorized access, disclosure

- Data
    - Integrity: Unauthorized modification, deletion
    - Confidentiality: Unauthorized access, disclosure
    - Availability: Data loss, corruption

- Network
    - Availability: Network failure, DoS
    - Confidentiality: Eavesdropping, monitoring
    - Integrity: Unauthorized modification, deletion

## Attack Surface Categories
- Network Attack Surface
    - Network protocols, services, ports
- Software Attack Surface
    - Application interfaces, libraries, services
- Human Attack Surface
    - Social engineering, phishing, insider threats

# Week 2 Topics

## Symmetric Encryption Process 
- Encryption: Plaintext -> Key -> Ciphertext
- Decryption: Ciphertext -> Key -> Plaintext

- Single key encryption, both sender and receiver use the same key to encrypt and decrypt the message
    - Example: DES, AES

## Block Cipher vs Stream Cipher
- Block Cipher: Encrypts fixed-size blocks of plaintext
    - Example: DES, AES

Stream Cipher: Encrypts plaintext one bit at a time
    - Example: RC4

## Hashing Algorithms
- One-way function, takes input and produces fixed-size output, contents of the output are unique to the input, used for data integrity
    - Example: MD5, SHA-1, SHA-256

## Public Key Encryption & Algorithms
- Asymmetric encryption, uses two keys, public and private, public key is used to encrypt, private key is used to decrypt
    - Example: RSA, ECC

## Digital Signatures and CA's Role in Digital Signatures
- Digital Signature: Hash of the message is encrypted with the sender's private key, used to verify the sender's identity and the integrity of the message

- Certificate Authority: Issues digital certificates, verifies the identity of the certificate holder

## Password Vulnerability 
- Weak passwords, dictionary attacks, brute force attacks, rainbow tables
-  Countermeasures: Password complexity, password hashing, salting

# Week 3 Topics

## Discretionary Access Control (Matrix & Control Structures)
- DAC: Access control based on the identity of the user and the user's relationship to the resource
    - Example: Unix file permissions
- Access Control Matrix: Rows represent subjects, columns represent objects, cells represent access rights

## Unix File Access Control
- Unique user ID, group ID, file permissions
    - Example: `chmod`, `chown`, `chgrp`

## Access Control Matrix Representation of RBAC
- RBAC: Access control based on the roles of the users
    - Example: `usermod`, `groupmod`, `rolemod`
- Matrix representation: Rows represent roles, columns represent permissions, cells represent access rights

## ABAC Policy Exmaple
- ABAC: Access control based on attributes of the user, resource, and environment
    - Example: `user.role == "admin" && resource.type == "file" && environment.time == "9:00 AM"`
- Can authorize access based on any attribute, not just roles, users, or resources
- Possible attributes: Subject attributes(User application), Object attributes(Device, network, domains), Environment attributes(Time, location, network)

## SQL Injection Attacks with Examples
- SQL Injection: Attacker injects SQL code into a web form input field, can be used to bypass authentication, access, modify, or delete data
    - Example: `SELECT * FROM users WHERE username = 'admin' OR 1=1; --'` (Will return all users)

## SQL Countermeasures
- Defensive Coding: Input validation, parameterized queries, stored procedures
- Detection: Web application firewalls, intrusion detection systems
- Runtime Prevention: Database firewalls, database activity monitoring

# Week 4 Topics

## Advanced Persistent Threats
- APT: Sophisticated, long-term cyber attacks, often state-sponsored, aimed at stealing data, disrupting operations, or causing damage
    - Example: Stuxnet, Flame, Duqu

## Viruses - Compontents and Classifications
- Virus: Malware that attaches itself to a host file, spreads when the host file is executed

- Components: Infection mechanism, trigger, payload
    - Infection Mechanism: How the virus spreads
    - Trigger: Event that activates the virus
    - Payload: Malicious action the virus performs

- Classifications: 
    - By Target: 
        - Boot Sector Virus: Infects the boot sector of a storage device
        - File Infector Virus: Infects executable files
        - Macro Virus: Infects documents and spreadsheets
    - By Concealment:
        - Encrypted Virus: Uses encryption to hide itself
        - Stealth Virus: Hides itself from detection
        - Polymorphic Virus: Changes its appearance with each infection
        - Metamorphic Virus: Completely changes its appearance to avoid detection

## Worms and Worm Replication
- Worm: Self-replicating malware that spreads over a network, does not need a host file to spread

- Replication:
    - Email Worm: Spreads through email
    - File Sharing Worm: Spreads through file sharing networks
    - Remote Execution Worm: Spreads through remote execution vulnerabilities
    - Remote File Access Worm: Spreads through remote file access vulnerabilities
    - Remote Login Worm: Logs onto a remote system and spreads from there

## Malvertising
- Malvertising: Malware delivered through online advertising, can be used to deliver ransomware, spyware, adware, etc.

## Clickjacking
- Clickjacking: Tricking a user into clicking on a link or button that is disguised as another link or button
    - Example, a transparent button over a legitimate button

## Payload Information Theft
- Keyloggers: Capture keystrokes
- Spyware: Capture screen shots, webcam images, microphone audio

## Countermeasures for Malware
- Ideal Countermeasure: Prevention

- Countermeasures:
    - Detection: Antivirus, intrusion detection systems
    - Identification: Digital signatures, hash values
    - Removal: Antivirus, malware removal tools

## DoS Attack Categories
- DoS: Denial of Service, attacker floods a system with traffic, causing it to become unresponsive

- Categories:
    - Network Bandwidth Consumption: Attacker floods the network with traffic
    - System Resource Consumption: Attacker consumes system resources, such as CPU, memory, disk space
    - Application Resource Consumption: Attacker consumes application resources, such as database connections, web server threads

## SYN Spoofing With Example
- SYN Spoofing: Attacker sends a SYN packet with a spoofed source IP address, causing the target to send a SYN-ACK to the spoofed address
    - TCP Handshake: SYN -> SYN-ACK -> ACK
    - Handshake is never completed, causing the target to consume resources
    - Example: `hping3 -S -a <spoofed IP> <target IP>`
    - Countermeasure: SYN cookies

## DNS Reflection Attack With Example
- DNS Reflection Attack: Attacker sends a DNS query to a DNS server with the source IP address spoofed to the target's IP address
    - DNS server responds to the target with the DNS query response
    - Example: `dig ANY <target domain> @<spoofed DNS server>`
    - Countermeasure: DNS Response Rate Limiting
    - Use DNS services to attack the target

## Dos Countermeasures, Defenses and Prevention
- Can not prevent all DoS attacks, but can mitigate the impact

Attack Prevention and Preemption:
    - Rate Limiting: Limit the number of requests a client can make
    - Traffic Shaping: Prioritize traffic based on type
    - Resource Management: Limit the resources a client can consume
    - Load Balancing: Distribute traffic across multiple servers
    - Redundancy: Have backup systems in place

Attack Detection and Filtering:
    - Anomaly Detection: Detect unusual traffic patterns
    - Signature Detection: Detect known attack patterns
    - Blackholing: Drop all traffic to the target
    - Sinkholing: Redirect traffic to a controlled system

Attack Source Traceback and Identification:
    - Packet Marking: Mark packets with source information
    - Packet Tracing: Trace packets back to their source
    - Packet Filtering: Drop packets from known attack sources

Attack Reaction
    - Traffic Diversion: Divert traffic to a controlled system
    - Traffic Analysis: Analyze traffic to identify attack patterns
    - Traffic Blocking: Block traffic from known attack sources

# Week 5 Topics

## Intrusion Detection System Types
- IDS: Monitors network traffic for signs of attacks or unauthorized access
    - Host Based IDS: Monitors a single host for signs of attacks
    - Network Based IDS: Monitors network traffic for signs of attacks
    - Distributed IDS: Monitors multiple hosts and networks for signs of attacks

## Analysis Approaches - Signature Based, Heuristic Based, Anomaly Based
- Signature / Hueristic Based: Detects known attack patterns
    - Example: Virus signatures, attack patterns
- Anomaly Based: Detects unusual patterns of network traffic
    - Example: Traffic volume, packet size, protocol usage

## Honeypots
- Honeypot: System designed to attract attackers, used to gather information about attack patterns and techniques
    - Example: Low-interaction, high-interaction, research, production

## Snort Rules
- Snort: Open-source IDS, uses rules to detect attack patterns
    - Example: `alert tcp any any -> any 80 (content:"GET /"; msg:"HTTP GET"; sid:1000001;)`

# Week 6 Topics

## Need of Firewalls
- Firewalls: Network security device that monitors and controls incoming and outgoing network traffic
    - Example: Packet filtering, stateful inspection, application layer filtering

## Firewall Filter Characteristics
- IP Address and Protocol: Source and destination IP addresses, source and destination ports, protocol
- Application Layer: Application layer protocols, application layer data
- User Identity: User authentication, user authorization
- Network Activity: Network activity patterns, network activity volume

## Packet Filtering Firewall
- Packet Filtering: Filters packets based on source and destination IP addresses, source and destination ports, protocol
    - Example: `iptables`, `firewalld`

## Stateful Connection Firewall
- Stateful Inspection: Filters packets based on the state of the connection
    - Example: `iptables`, `firewalld`

## Host and Network Based IPS
- IPS (Intrusion Prevention System): Monitors network traffic for signs of attacks and unauthorized access, can take action to prevent attacks
    - Host Based IPS: Monitors a single host for signs of attacks
    - Network Based IPS: Monitors network traffic for signs of attacks

## Buffer Overflow Attack with Example Code
- Buffer Overflow: Attacker sends more data to a buffer than it can handle, overwriting adjacent memory
    - Example: `char buffer[8]; strcpy(buffer, argv[1]);` (Buffer overflow if `argv[1]` is longer than 8 characters)

# Week 7 Topics

## List Any 5 OWASP Coding Practices For Input Validation
- Input Validation: Validate input to prevent injection attacks
    - Example: SQL injection, XSS, CSRF

- OWASP Practices:
    - Validate on server side
        - Never trust client input and perform validation on the server side (e.g. JavaScript validation can be bypassed)
    - Classify and Validate Data Sources
        - Identify where your data comes from and validate it accordingly, Untrusted data should be validated more strictly (e.g. user input vs database query)
    - Use Centralized Data Validation
        - Use a centralized data validation library to ensure consistency (e.g. OWASP ESAPI)
    - Specify Character Sets
        - Specify the character set that is allowed for input (e.g. alphanumeric, special characters)
    - Reject Invalid Input
        - Reject input that does not conform to the expected format (e.g. If data fails do not process it)

## Logging
- Logging: Recording events and data for analysis and troubleshooting
    - Example: System logs, application logs, security logs

## Virtualization - VMs VS Containers
- Virtual Machines: Emulate a physical computer, run an operating system and applications
    - Example: VMware, VirtualBox, Hyper-V
- Containers: Run applications in isolated environments, share the host OS kernel
    - Example: Docker, Kubernetes

## Cloud Service Models (IaaS, PaaS, SaaS)
- IaaS: Infrastructure as a Service, provides virtualized computing resources over the internet
    - Example: AWS EC2, Azure VM
- PaaS: Platform as a Service, provides a platform for developing, running, and managing applications
    - Example: AWS Elastic Beanstalk, Azure App Service
- SaaS: Software as a Service, provides software over the internet
    - Example: Office 365, Salesforce

## Comparison of Cloud Deployment Models
- Public Cloud: Cloud services are provided over the internet
- Private Cloud: Cloud services are provided over a private network
- Hybrid Cloud: Combination of public and private cloud services
- Community Cloud: Cloud services are shared by a specific community

## Cloud vs Fog Computing
- Fog Computing: Extends cloud computing to the edge of the network, closer to the data source
    - Example: IoT devices, edge computing

Cloud vs Edge Computing
- Edge Computing: Processing data closer to the data source, reduces latency
    - Example: IoT devices, mobile devices
- Cloud Computing: Processing data over the internet, provides scalability and flexibility
    - Example: AWS, Azure

