## Web Backend Development

# Scalability 
Scalability - ability to adjust the capacity of the system to cost efficiently fulfill the demands 
* Handling more data 
* Handling higher concurrency levels
* Handling higher interactivity levels

# Virtual Private Server
Virtual Private Server (VPS) - a virtual machine sold as a service by an Internet hosting service, hosted together with other virtual machines on the same physical server

# Single Server Setup 
Web pages, images, css, js, etc. are served by a single server

As user base grows, the server will be overloaded and the website will be slow, or even crash

# Making Server Stronger 
Vertical Scalability - adding more resources to the server, such as CPU, memory, disk space, etc.
    Issues:
    * Limited by the hardware
    * Costly


Horizontal Scalability - adding more servers to the system

# Lock and Lock Contention
Locks - are used to synchronize access to shared resources or data structures
Lock contention - performance bottleneck caused by inefficient use of locks

Vertical Scalability does not affect system architecture, but Horizontal Scalability does

# Isolation of Services
Isolation of services - each service is independent of each other, and can be scaled independently

# Functional Partitioning
Functional partitioning - process of dividing a system based on functionality to scale each part independently

# Cache 
Cache - server/service focused on reducing latency and resources needed to generate the result of a request

# Content Delivery Network
Content Delivery Network (CDN) - a geographically distributed network of proxy servers and their data centers, used to distribute service spatially relative to end-users to provide high availability and high performance

# Round Robin DNS
Round Robin DNS - a technique of load distribution, load balancing, or fault-tolerance provisioning multiple, redundant Internet Protocol service hosts, e.g., Web server, FTP servers, by managing the Domain Name System's (DNS) responses to address requests from client computers according to an appropriate statistical model

# GeoDNS
GeoDNS - a Domain Name System (DNS) technology that lets DNS queries be answered based on the geographic location of both the DNS query and the location of the DNS resolver

# Front Line
Front Line - a service that sits in front of the application servers and handles requests from the clients, does not have any business logic, and is used to improve performance, reliability, and security

# Load Balancer
Load Balancer - software or hardware component that distributes traffic coming to a single IP address over multiple servers, which are hidden behind the load balancer. It is used to share the load between the servers and to make the system more reliable

# Web Application Layer
Web Application Layer - consists of web application servers, which are responsible for generating the actual HTML of the web application and handle client requests

# Web Service Layer
Web Service Layer - consists of web service servers, which are responsible for handling business logic and data access

# Object Cache 
Object Cache - used by both front-end application servers and web services to reduce the load on the database and improve performance

# Message Queue 
Message Queue - used to postpone some of the processing to a later stage and to delegate work to queue workers

# Application Architecture Types
Service Oriented Architecture (SOA) - an architectural pattern in computer software design in which application components provide services to other components via a communications protocol, typically over a network

# Hexagonal Architecture
Hexagonal Architecture - an architectural pattern used to build applications around a core business logic, which is isolated from the external environment by adapters

# Event Driven Architecture
Event Driven Architecture (EDA) - a software architecture paradigm promoting the production, detection, consumption of, and reaction to events, Does not need to wait for a response from the server, and can continue to work with the user

