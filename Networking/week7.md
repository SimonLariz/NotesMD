## Week 7 

# Dynamic Routing Overview

Dynamic Routing - routing that can adapt to changes in the network, scales well and is robust.

Administrative Distance - A metric used by routers to determine which route to use if there are multiple routes to the same destination. The route with the lowest administrative distance is used.

# Types of Dynamic Routing

Distance Vector Routing - Each router computer distance to it next immediate neighbors (RIP, EIGRP, BGP)

Advantages:
- Simple
- Low memory and CPU requirements
- Low bandwidth requirements

Disadvantages:
- Slow adjustment to network changes

Link State Routing - Each router shares knowledge of its neighbors with all other routers in the network (OSPF, IS-IS)

How does OSFP create a topology map?
1. Acquire neighbor relationship to exchange network information, eg. two routers running OSPF on the same network segment will become neighbors
    i. Manually set router to higher priority
    ii. Manually set the router ID
    iii. Set by choosing the highest up status loopback interface
    iv. Set by choosing the highest up status non-loopback interface
2. Exchange database information, Neighboring routers swap LSDB information
3. Calculate the shortest path to each network, Each router uses the LSDB to calculate the shortest path to each network

Administrative distance for OSPF the speed of interface, the lower the speed the higher the administrative distance

# OSPF Guide

```
config terminal
router ospf 1
router-id 1.1.1.1
interfaace f0/0
ip address 192.168.1.1 255.255.255.252
ip ospf 1 area 0
no shutdown
exit

```