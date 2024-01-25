# Pentesting 

Vulnerability Assessment - review of system services to find potential vulnerabilities without attempts at exploitation.

Penetration Testing - Finding and exploiting system vulnerabilities as proof-of-concept.

White box - penetration tester is given access to all information about the system being tested.
    Advantage: Very through
    Disadvantage: Not completely realistic, the tester is not in the same position as the attacker, who typically starts with little to no information about the system.

Black box - penetration tester is given no information about the system.
    Advantage: realistic, the tester is in the same position as the attacker.
    Disadvantage: lack of knowledge of the system's inner workings, precludes the tester from testing some areas of the system.

Ethical vs Unethical Hacking
    Ethical hacking - hacking with permission
        Motivation: to improve the security of the system
    Unethical hacking - hacking without permission
        Motivation: to gain access to the system for personal gain
    
Penetration Testing Frameworks - a set of tools and procedures for penetration testing 

Penetration Testing Overview
1. Reconnaissance - gather information about the target
    Passive - gather information without directly interacting with the target (Google-Fu, social media, etc.)
    Active - gather information by directly interacting with the target (port scanning, etc. not always legal)

2. Scanning - identify open ports and services
    Network Vulnerability Scanning - identify vulnerabilities in network services
        Open Source: OpenVAS, Nmap
        Commercial: Nessus, Qualys
    Web Vulnerability Scanning - identify vulnerabilities in web services
        Nikto, WPScan, Burp Suite, Zed Attack Proxy

3. Exploitation - attempt to exploit vulnerabilities

4. Post-exploitation - attempt to maintain access to the system

5. Reporting - document the findings

# Intrusion Detection 

Security Intrusion - a security event that monitors and analyzes system events for the purpose of finding, and providing real-time or near real-time warning of, attempts to access system resources in an unauthorized manner.

Intrusion Prevention - an intrusion detection system that also attempts to stop detected possible incidents.

Signature Detection - Observe events on system and applying a set of rules to decide if intruder approaches:
    Rule-based anomaly detection - Analyze audit logs and compare to a set of rules
    Statistical anomaly detection - Analyze audit logs and compare to a statistical model of normal behavior

Rule based penetration testing - a set of rules that define what is considered an intrusion
    Examples:
        Users should not read files in other users' home directories
        User must not write to other's files
        User must not execute programs in other users' directories
        User must not execute programs in /tmp

Intrusion Detection System - Sniffs and reports possible violations

Intrusion Prevention System - Sniffs and reports possible violations and attempts to stop them

What an IDS Cannot Detect
    - Passwords which were not changed from default
    - File transfer of confidential data
    - Social engineering
    - Decipher encrypted messages on a network




