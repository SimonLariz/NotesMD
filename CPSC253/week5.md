## Week 5

# APT 
- Advanced Persistent Threat
- APT is a stealthy computer network threat actor, typically a nation state or state-sponsored group, which gains unauthorized access to a computer network and remains undetected for an extended period.
- APTs are usually directed at organizations and are done for the purpose of espionage or stealing data.
- Consist of zero-day exploits, malware, and social engineering.

# Viruses
- Piece of software that infects a computer and then spreads to other computers.
* Modifies them to include a copy of the virus.
* Replicates itself and spreads to other computers.
* Easily spread through networks, email, and the internet.
- When attached to an executable file, the virus can do anything the program can do.
- Can be used to steal information, harm the host computer, or create a backdoor for hackers.

# Virus Components 
- Infection Mechanism: How the virus spreads aka Infection Vector.
- Trigger: What causes the virus to activate and spread 
- Payload: What the virus does when it activates.

# Virus Phases
- Dormant Phase: The virus is idle. The virus will eventually be activated by some event, such as a date, the presence of another program or file, or the capacity of the disk exceeding some limit.

- Triggering Phase: The virus is activated to perform the function for which it was intended.

- Propagation Phase: The virus places an identical copy of itself into other programs or into certain system areas on the disk. Each infected program will now contain a clone of the virus, which will itself enter a propagation phase.

- Execution Phase: The function is performed. The function may be harmless, such as a message on the screen, or damaging, such as the destruction of programs and data files.

# Macro Virus
- A macro virus is a computer virus written in the same macro language used for software applications, such as word processors.

# Virus Classifications
Classification by Target:
- Boot Sector Virus: Infects the boot sector of a hard disk or floppy disk.
- File Infector Virus: Infects executable files.
- Macro Virus: Written in the same macro language used for software applications.
- Multipartite Virus: Infect files in multiple ways.

Classification by Concealment Strategy:
- Encrypted Virus: Hides from antivirus software by encrypting its code.
- Stealth Virus: Hides from antivirus software by intercepting its requests.
- Polymorphic Virus: Hides from antivirus software by changing its code.
- Metamorphic Virus: Hides from antivirus software by changing its appearance.

# Worms
- A worm is a standalone malware computer program that replicates itself in order to spread to other computers.
- Often uses a computer network to spread itself, relying on security failures on the target computer to access it.
- Worms almost always cause at least some harm to the network, even if only by consuming bandwidth, whereas viruses almost always corrupt or modify files on a targeted computer.

# Worm Terminology
Multipplatform - Can infect multiple operating systems.
Multi-exploit - Can use multiple methods to spread.
Ultrafast - Can spread very quickly.
Polymorphic - Can change its appearance to avoid detection.
Metamorphic - Can change its code to avoid detection.
Transport Vehicle - Can carry other malware.

# Worm Replication
Worms can replicate in the following ways:
- Email: Send itself to everyone in the victim's address book.
- File Sharing: Copy itself to shared folders.
- Remote Execution: Copy itself to other computers using remote execution.
- Remote file copy: Copy itself to other computers using file sharing.
- Remote login: Copy itself to other computers using remote login.

# Worm Target Discovery
Scanning (Fingerprinting) - The worm scans the network to find other computers to infect.
- Random Scanning: The worm scans random IP addresses.
- Hitlist Scanning: The worm scans a list of IP addresses.
- Topological Scanning: The worm scans based on network topology.
- Local Subnet Scanning: The worm scans the local subnet.

# Morris Worm
- The Morris worm or Internet worm of November 2, 1988, was one of the first computer worms distributed via the Internet.
- It was written by a student at Cornell University, Robert Tappan Morris, and caused the first denial of service (DoS) attack on the Internet.

# WannaCry
- WannaCry is a ransomware attack that spread rapidly through a number of computer networks in May of 2017.
- Spread as a worm, it used the EternalBlue exploit to target computers running the Microsoft Windows operating system.
- The attack was estimated to have affected more than 200,000 computers across 150 countries, with total damages ranging from hundreds of millions to billions of dollars.

# Mobile Code
- Mobile code is any program, such as a script or macro, that can be transmitted and executed on a computer without the user's knowledge or consent.
- Most common types of mobile code are cross-site scripting (XSS), interactive and static web content, and Java applets.

# Mobile Phone Worms
- A mobile phone worm is a piece of malware that infects mobile phones and then spreads to other phones.
- Mobile phone worms can spread through text messages, email, and Bluetooth.

# Drive By Downloads
- A drive-by download is a download that happens without a person's knowledge.

# Malvertising
- Malvertising is the use of online advertising to spread malware and viruses.

# Clickjacking
- Clickjacking is a malicious technique of tricking a user into clicking on something different from what the user perceives, thus potentially revealing confidential information or taking control of their computer while clicking on seemingly innocuous web pages.
- Attacker can create a transparent layer over a legitimate website and trick the user into clicking on a button or link on another page.

# Keyloggers
- A keylogger is a type of surveillance software that records every keystroke made by a user, often without their knowledge. 

# Spyware
- Spyware is software that aims to gather information about a person or organization without their knowledge and that may send such information to another entity without the consumer's consent, or that asserts control over a device without the consumer's knowledge.

# Remote Control Facility 
- Distinguishes a bot from a worm.
- Worm propagates itself, but a bot is controlled by a remote attacker.

# Rookit
- A rootkit is a collection of computer software, typically malicious, designed to enable access to a computer or an area of its software that is not otherwise allowed and often masks its existence or the existence of other software.

Rootkit:
- Persistent 
- Memory-based
- User-mode
- Kernel-mode

# Counter Measures to Malware
Ideal solution is prevention

# Anti-Virus Software
First generation: Signature-based
Second generation: Heuristic-based
Third generation: Activity-based
Fourth generation: Full-featured protection

# Perimeter Scanning Approaches
Ingress Monitoring: Scans incoming traffic.
Egress Monitoring: Scans outgoing traffic.
