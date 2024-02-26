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