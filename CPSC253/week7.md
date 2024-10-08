## Week 7 Notes

# Placement of Malware Monitors
- malware monitors are placed in the network to detect malware
- they can be placed at the edge of the network, at the core of the network, or at the endpoint

# Buffer Overflow
- buffer overflow is a type of attack that occurs when a program writes more data to a buffer than it can hold
- this can cause the program to crash or allow an attacker to execute arbitrary code
- buffer overflow attacks can be prevented by using safe programming practices and by using tools like ASLR and DEP

# Runtime Defenses for Buffer Overflow
- Address Space Layout Randomization (ASLR) is a security feature that randomizes the memory layout of a program to make it harder for an attacker to predict the location of code and data

- Data Execution Prevention (DEP) is a security feature that prevents code from being executed in certain areas of memory, such as the stack and heap

- Stack Canaries are a security feature that adds a random value to the stack to detect buffer overflow attacks

# Heap Overflow
- heap overflow is a type of buffer overflow attack that occurs in the heap memory
- it can be used to corrupt data structures and cause the program to crash or execute arbitrary code

# OWASP Coding Practices
- OWASP provides a list of secure coding practices to help developers write secure code
- some of the key practices include input validation, output encoding, and using secure libraries

# Defensive Programming
- defensive programming is a set of coding practices that are designed to make software more resilient to attacks

- Input validation
- Correct data interpretation
- Handling race conditions
- Shell script execution vulnerabilities
- Use of privileged user accounts
- File IO
- Memory management

# OS Security Layers
- User applications
- System libraries
- Kernel
- Hardware

# Logging 
- Logging is the process of recording events that occur in a system
- Logging is important for security monitoring and incident response
- Some best practices for logging include using a centralized logging system, logging at different levels of detail, and protecting log files from tampering
- Automated analysis of logs can help identify security incidents and trends 

# Windows Security User Account Control (UAC)
- User Account Control (UAC) is a security feature in Windows that helps prevent unauthorized changes to the system
- UAC prompts the user for permission before allowing certain actions to be performed
- UAC can help prevent malware from making unauthorized changes to the system

# Virtualization
- Virtualization is the process of creating a virtual version of a physical resource, such as a server, storage device, or network
- Benefits of virtualization include cost savings, improved resource utilization, and increased flexibility
- Provides support for multiple distinct virtual machines on a single physical machine
- Raises additional security concerns

# Containers 
- Containers are a lightweight form of virtualization that allows applications to be run in isolated environments
- Containers are often used in cloud environments to provide a consistent runtime environment for applications
- Containers can help improve security by isolating applications from each other and from the underlying operating system


# Cloud Computing
- Cloud computing is the delivery of computing services over the internet
- Benefits of cloud computing include cost savings, scalability, and flexibility
- Security concerns include data privacy, data breaches, and compliance with regulations
- Examples of cloud computing services include Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS)
- EX: AWS, Azure, Google Cloud

# IaaS, PaaS, SaaS
- Infrastructure as a Service (IaaS) provides virtualized computing resources over the internet
- Platform as a Service (PaaS) provides a platform for developing, testing, and deploying applications
- Software as a Service (SaaS) provides software applications over the internet

# Security Concerns in Cloud Computing
- Data privacy
- Availability
- Data breaches
- Businesses should perform due diligence when selecting a cloud provider and should implement security controls to protect their data
- Cloud providers should implement security controls to protect their customers' data
- Security controls should be implemented at the network, host, and application layers

# The Internet of Things (IoT)
- The Internet of Things (IoT) refers to the network of physical objects that are connected to the internet
- The objects deliver sensor data to the cloud, where it can be analyzed and acted upon
- The IoT is primarily used in the context of consumer electronics, such as smart home devices and wearables

# Fog 
- In many IoT applications, the data generated by the devices needs to be processed and analyzed in real time
- Fog computing is a distributed computing infrastructure that extends the cloud to the edge of the network
- Fog computing can help reduce latency and improve the performance of IoT applications

# Cloud vs Fog
- Cloud computing is a centralized computing model that provides computing resources over the internet
- Fog computing is a distributed computing model that extends the cloud to the edge of the network 

# Iot Gateway Security
- IoT gateways are devices that connect IoT devices to the cloud
- They can provide security features such as encryption, authentication, and access control
