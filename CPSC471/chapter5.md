## Chapter 5: Network Layer

## Network Layer Functions
- Forwarding: Move packets from router's input to appropriate router output
- Routing: Determine route taken by packets from source to destination

- Per-router control plane: Individual routing algorithm components in each and every router (traditional routing algorithms)
- Logically centralized control plane: Network-wide logic in a single place (software-defined networking)

## Per-router control plane
- Individual routing algorithm components in each and every router
- Router will have information on nearby routers and the cost to reach them

## Software Defined Networking (SDN)
- Remote controller computes, installs routing tables in routers
- OpenFlow: Protocol for remote controllers to modify routing tables

## Inter-AS routing: Routing within an Autonomous System (AS)
Common intra-AS routing protocols:
- RIP (Routing Information Protocol)
- EIGRP (Enhanced Interior Gateway Routing Protocol)
- OSPF (Open Shortest Path First)

## OSPF (Open Shortest Path First)
- "Open": publicly available
- Classic link state
    - each router floods link state information to all other routers in the entire AS
    - multiple link costs metrics (delay, bandwidth, etc.)
    - OSPF path computation: Dijkstra's algorithm,
- Security: all OSPF messages authenticated (to prevent malicious intrusion)

## Hierarchical OSPF
- Two-level hierarchy: local area and backbone
    - Link-state advertisements only in area
    - Each node has detailed area topology; only know direction (shortest path) to nets in other areas

## Internet inter-AS routing: BGP (Border Gateway Protocol)
- BGP: the de facto inter-domain routing protocol
- Allows subnet to advertise its existence to rest of the Internet
- Allows subnet to learn paths to other subnets

## Path attributes and BGP routes 
- BGP advertised route: prefix + attributes
    - prefix: destination being advertised
    - two important attributes: AS-PATH, NEXT-HOP
- AS-PATH: list of ASes through which prefix advertisement has passed
- NEXT-HOP: the next router to send packet to, on way to advertised prefix

## Software Defined Networking Control Plane
- SDN: logically centralized control plane
- SDN controller: computes routing tables, installs them in routers
- Central controller allows for easier network management, faster network reconfiguration, and easier network troubleshooting
- Allows for load balancing, traffic engineering, and easier network management

## SDN: Select challenges
- Hardening the control plane, dependable, reliable, performance-scalable control plane
- Networks, protocols, and meeting mission specific requirements
- Security, privacy, and trustworthiness

## ICMP: Internet control message protocol
- Used by hosts and routers to communicate network-level information

Bellman ford equation has value for ________ routing
- Distance vector

Dijkstra's algorithm has value for ________ routing
-