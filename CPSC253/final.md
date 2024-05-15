# Exam Format 
    - 6 Answer in brief questions
    - 2 Numerical problems
    - 2 Application / Scenario based questions

## Week - 8
- Risk Assessment: Approaches to identifying and mitigating risks to an organization's IT infrastructure
- Risk Management: Strategies for managing risks to an organization's IT infrastructure
- Risk Mitigation: Techniques for reducing risks to an organization's IT infrastructure
- Risk Response: Strategies for responding to risks to an organization's IT infrastructure

- Risk Register: A document that lists the risks to an organization's IT infrastructure and the strategies for managing them
Example: 
    - Risk: Unauthorized access to the organization's IT infrastructure
    - Strategy: Implementing access controls and monitoring systems

## Week - 9 
- Security Implementation Plan: A document that outlines the steps for implementing security measures to protect an organization's IT infrastructure
Example: 
    - Step 1: Identify the security requirements of the organization
    - Step 2: Develop a security policy
    - Step 3: Implement security measures
    - Step 4: Monitor and evaluate the security measures

- Security Compliance: Ensuring that an organization's IT infrastructure complies with relevant security standards and regulations
    - Checking process: 
        - Step 1: Identify the relevant security standards and regulations
        - Step 2: Assess the organization's IT infrastructure against the standards and regulations
        - Step 3: Implement the necessary security measures to comply with the standards and regulations
        - Step 4: Monitor and evaluate the organization's compliance with the standards and regulations

- Change vs Configuration Management: 
    - Change Management: The process of managing changes to an organization's IT infrastructure
    - Configuration Management: The process of managing the configuration of an organization's IT infrastructure

## Week - 10 
- Physical and Infrastructure Security: 
    - Physical Security: Measures to protect an organization's IT infrastructure from physical threats
        Example: 
            - Installing security cameras
            - Implementing access controls
            - Using biometric authentication
    - Infrastructure Security: Measures to protect an organization's IT infrastructure from cyber threats
        Example: 
            - Implementing firewalls
            - Using intrusion detection systems
            - Encrypting data
- Physical Security Threats(Environmental, Technical, Human)
    - Environmental Threats: Threats to an organization's IT infrastructure from natural disasters
        Example: 
            - Earthquakes
            - Floods
            - Fires
    - Technical Threats: Threats to an organization's IT infrastructure from technical failures
        Example: 
            - Hardware failures
            - Software failures
            - Power outages
    - Human Threats: Threats to an organization's IT infrastructure from human actions
        Example: 
            - Unauthorized access
            - Insider threats
            - Social engineering attacks
- Benefits of security Awareness training and Education Programs
    - Benefits: 
        - Increased awareness of security risks
        - Improved security practices
        - Reduced security incidents
        - Enhanced security culture
- Email and Internet Use Policies
    - Email Use Policy: A document that outlines the rules and guidelines for using email in an organization
        Example: 
            - Do not open suspicious emails
            - Do not share sensitive information via email
            - Do not use personal email for work purposes
    - Internet Use Policy: A document that outlines the rules and guidelines for using the internet in an organization
        Example: 
            - Do not visit unauthorized websites
            - Do not download unauthorized software
            - Do not share sensitive information online
        
## Week - 12
- Auditable Items
    - Auditable Items: Items in an organization's IT infrastructure that can be audited for compliance with security standards and regulations
        Example: 
            - User accounts
            - Access controls
            - Security logs
- Intellectual Property Infringement
    - Intellectual Property Infringement: Unauthorized use of an organization's intellectual property
        Example: 
            - Copying software without permission
            - Using copyrighted material without permission
            - Selling counterfeit products
- Ethical Issues
    - Ethical Issues: Moral dilemmas related to the use of technology in an organization
        Example: 
            - Privacy concerns
            - Data security
            - Intellectual property rights

## Week - 13
- Symmetric vs Asymmetric Encryption
    - Symmetric Encryption: A type of encryption where the same key is used for both encryption and decryption
    - Asymmetric Encryption: A type of encryption where a public key is used for encryption and a private key is used for decryption
- AES Encryption 4 Functions
    - AES Encryption: A symmetric encryption algorithm used to secure data
        - Key Expansion: Expands the key to generate round keys for each round of encryption
        - SubBytes: Substitutes each byte of the state with a corresponding byte from the S-box
        - ShiftRows: Shifts the rows of the state to create a diffusion effect
        - MixColumns: Mixes the columns of the state to create confusion
- SHA & HMAC
    - SHA: Secure Hash Algorithm used to generate a fixed-size hash value from input data
    - HMAC: Hash-based Message Authentication Code used to verify the integrity and authenticity of a message
- One-way Hash Functions
    - One-way Hash Functions: Functions that generate a fixed-size hash value from input data, but cannot be reversed to obtain the original data
        Example: 
            - MD5
            - SHA-1
            - SHA-256
- RSA
    - How to compute RSA
        - Step 1: Generate two large prime numbers, p and q
        - Step 2: Compute n = p * q
        - Step 3: Compute φ(n) = (p-1) * (q-1)
        - Step 4: Choose an encryption key, e, such that 1 < e < φ(n) and gcd(e, φ(n)) = 1
        - Step 5: Compute the decryption key, d, such that d * e ≡ 1 (mod φ(n))
        - Step 6: The public key is (n, e) and the private key is (n, d)
        - Step 7: To encrypt a message m, compute c = m^e mod n
        - Step 8: To decrypt a ciphertext c, compute m = c^d mod n
    
    Example:
        - p = 7 and q = 11
        - n = p * q = 7 * 11 = 77
        - φ(n) = (p-1) * (q-1) = 6 * 10 = 60
        - e = 13
        - d = 37
        - Public key: (77, 13)
        - Private key: (77, 37)
        - Encryption: c = 5^13 mod 77 = 5
        - Decryption: m = 5^37 mod 77 = 5

- Diffie-Hellman Problem
    - How to compute Diffie-Hellman
        - Step 1: Choose a prime number, p, and a primitive root modulo p, g
        - Step 2: Alice chooses a secret key, a, and computes A = g^a mod p
        - Step 3: Bob chooses a secret key, b, and computes B = g^b mod p
        - Step 4: Alice and Bob exchange A and B
        - Step 5: Alice computes the shared secret, s, as s = B^a mod p
        - Step 6: Bob computes the shared secret, s, as s = A^b mod p
        - Step 7: Alice and Bob now have a shared secret key, s
    
    Example:
        - p = 23 and g = 5
        - Alice chooses a = 6 and computes A = 5^6 mod 23 = 8
        - Bob chooses b = 15 and computes B = 5^15 mod 23 = 19
        - Alice computes the shared secret, s, as s = 19^6 mod 23 = 2
        - Bob computes the shared secret, s, as s = 8^15 mod 23 = 2

## Week - 14
-SMTP, MIME, S/MIME
    - SMTP: Simple Mail Transfer Protocol used to send and receive email messages
    - MIME: Multipurpose Internet Mail Extensions used to encode multimedia content in email messages
    - S/MIME: Secure/Multipurpose Internet Mail Extensions used to encrypt and sign email messages
- DKIM
    - DKIM: DomainKeys Identified Mail used to verify the authenticity of email messages
- SSL & TLS
    - SSL: Secure Sockets Layer used to secure data transmitted over the internet
    - TLS: Transport Layer Security used to secure data transmitted over the internet
- TLS Handshake
    - TLS Handshake: The process of establishing a secure connection between a client and a server using the TLS protocol
- Heartbeat & Heartbleed
    - Heartbeat: A feature of the TLS protocol used to keep a connection alive
    - Heartbleed: A security vulnerability in the OpenSSL library that allows an attacker to read sensitive data from a server's memory
- HTTPS
    - HTTPS: Hypertext Transfer Protocol Secure used to secure data transmitted over the internet
- IPsec
    - IPsec: Internet Protocol Security used to secure data transmitted over IP networks
- Transport vs Tunnel Mode
    - Transport Mode: Encrypts only the data payload of an IP packet
    - Tunnel Mode: Encrypts the entire IP packet
- Kerberos
    - Kerberos: A network authentication protocol used to verify the identity of users and services
    - Working Example: 
        - Step 1: The client requests a ticket-granting ticket (TGT) from the Key Distribution Center (KDC)
        - Step 2: The KDC issues a TGT to the client
        - Step 3: The client requests a service ticket from the Ticket Granting Server (TGS)
        - Step 4: The TGS issues a service ticket to the client
        - Step 5: The client presents the service ticket to the service for authentication
        - Step 6: The service grants access to the client
- Certificate Authorities
    - Certificate Authorities: Organizations that issue digital certificates to verify the identity of users and services
    - Working Example: 
        - Step 1: The user requests a digital certificate from the CA
        - Step 2: The CA verifies the user's identity
        - Step 3: The CA issues a digital certificate to the user
        - Step 4: The user presents the digital certificate to the service for authentication
        - Step 5: The service verifies the digital certificate with the CA
        - Step 6: The service grants access to the user
- X.509
    - X.509: A standard format for digital certificates that includes information about the certificate holder

## Week - 15
- Wireless LAN Attacks
    - Attacks: 
        - Eavesdropping
            - Listening to wireless communications to capture sensitive information
        - Evil Twin
            - Creating a fake wireless access point to intercept communications
        - Rogue Access Point
            - Setting up an unauthorized access point to capture data
        - Denial of Service
            - Disrupting wireless communications to prevent access
        - Car Driving
            - Driving around to capture wireless signals
- Wireless Network Threats
    - Threats: 
        - Accidental Association
            - Connecting to an unauthorized wireless network
        - Malicious Association
            - Connecting to a malicious wireless network
        - Ad-Hoc Networks
            - Creating an ad-hoc wireless network to bypass security controls
        - Nontraditional Networks
            - Using nontraditional wireless networks to access sensitive information
        - Identity Theft
            - Stealing wireless credentials to impersonate a user
        - Man-in-the-Middle
            - Intercepting wireless communications to capture sensitive information
        - Network Injection
            - Injecting malicious data into wireless communications
- Phases of Operation
    - Phase 1: Discovery
        - Identifying wireless networks in the area
    - Phase 2: Authentication
        - Attempting to connect to wireless networks
    - Phase 3 Key Management
        - Obtaining encryption keys to access wireless networks
    - Phase 4: Protected Data Transfer
        - Capturing sensitive information from wireless networks
    - Phase 5: Disconnection
        - Disconnecting from wireless networks to avoid detection
- Linux DAC
    - Discretionary Access Control (DAC): A security model that allows users to control access to their own resources
- Simple File Permissions, Directory Permissions, Modes, Special Permissions
    - Simple File Permissions: Permissions that control access to files in a Linux system
    - Directory Permissions: Permissions that control access to directories in a Linux system
    - Modes: 
        - Read
        - Write
        - Execute
    - Special Permissions:
        - Setuid: Allows a user to execute a file with the permissions of the file owner
        - Setgid: Allows a user to execute a file with the permissions of the file group
        - Sticky Bit: Prevents users from deleting files they do not own
    - Numeric modes 
        - 0: No permissions
        - 1: Execute only
        - 2: Write only
        - 3: Write and execute
        - 4: Read only
        - 5: Read and execute
        - 6: Read and write
        - 7: Read, write, and execute
- Linux Vulnerabilities
    - Buffer Overflow
        - A vulnerability that allows an attacker to overwrite memory beyond the bounds of a buffer
    - Race Condition
        - A vulnerability that occurs when two processes access the same resource at the same time
    - Abuse of programs run "setuid"
        - A vulnerability that allows an attacker to execute a file with elevated privileges
    - Denial of Service
        - A vulnerability that disrupts the availability of a system or service
    - Web Application Vulnerabilities
        - A vulnerability that allows an attacker to exploit a web application
    - Rootkits
        - A vulnerability that allows an attacker to gain root access to a system
- Windows Security
    - Windows Security: Measures to protect an organization's IT infrastructure running on Windows operating systems
    - Defenses: 
        - User Account Control
        - Windows Firewall
        - Windows Defender
        - BitLocker
        - AppLocker
        - Windows Update
        - Windows Security Center
- Windows Security Defenses
    - User Account Control: A feature that prompts users for permission before allowing applications to make changes to the system
    - Windows Firewall: A feature that filters incoming and outgoing network traffic to protect the system
    - Windows Defender: An antivirus program that protects the system from malware
    - BitLocker: A feature that encrypts the system drive to protect data

