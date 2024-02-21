## Week 6 Firewalls and Intrusion Prevention Systems

# Firewall Access Policy
- Firewall access policy is a set of rules that define what traffic is allowed to pass through the firewall and what traffic is blocked.
- Firewall access policy is typically defined in terms of source and destination IP addresses, source and destination port numbers, and the protocol used.
- Policies can be defined in terms of:
  - Allow: Traffic is allowed to pass through the firewall.
  - Deny: Traffic is blocked from passing through the firewall.
  - Drop: Traffic is silently discarded by the firewall.
  - Reject: Traffic is blocked and the sender is notified that the traffic was blocked.

# Firewall Filtering Characteristics
- Application Protocol Filtering: Filters traffic based on the application protocol used.
- User Identity Filtering: Filters traffic based on the user's identity.
- Network Activity Filtering: Filters traffic based on the network activity.

# Packet Filtering Firewall
- Packet filtering firewall is a type of firewall that filters traffic based on the source and destination IP addresses, source and destination port numbers, and the protocol used.
- Packet filtering firewall is typically implemented in a router or a dedicated firewall appliance.

Trade-offs of Packet Filtering Firewall:
- Pros:
  - Low cost
  - Low latency
- Cons:
    - Limited filtering capabilities
    - Vulnerable to IP spoofing
    - Vulnerable to DoS attacks
    - Does not allow user authentication

# Stateful Inspection Firewall
- Stateful inspection firewall is a type of firewall that filters traffic based on the state of the connection.
- Stateful inspection firewall maintains a state table that keeps track of the state of each connection.
- Stateful inspection firewall is typically implemented in a dedicated firewall appliance.

Trade-offs of Stateful Inspection Firewall:
- Pros:
  - Better filtering capabilities
  - Better protection against IP spoofing
  - Better protection against DoS attacks
  - Allows user authentication
- Cons:
    - Higher cost
    - Higher latency

# Application Level Gateway Firewall
- Application level gateway firewall is a type of firewall that filters traffic based on the application protocol used.

# Circuit Level Gateway Firewall
- Circuit level gateway firewall operates at the transport layer of the OSI model and is used to filter traffic based on the state of the connection.

# Personal Firewall
- Personal firewall is a type of firewall that is installed on an individual computer to protect it from unauthorized access.



OSI Model:
- Application Layer
- Presentation Layer
- Session Layer
- Transport Layer
- Network Layer
- Data Link Layer
- Physical Layer

