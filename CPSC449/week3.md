## HTTP Protocol

# OSI Model
- Application Layer
- Presentation Layer
- Session Layer
- Transport Layer
- Network Layer
- Data Link Layer
- Physical Layer

# TCP/IP Model
- Application Layer
- Transport Layer
- Internet Layer
- Network Access Layer

# Application Layer
Application layer is the top most layer of OSI model. It provides the interface between the applications and the network. It provides the services directly to the user

# HTTP
HTTP - Hyper Text Transfer Protocol, is a protocol used for transferring hypertext documents over the internet. It is a stateless protocol, which means that the server does not keep any data between two requests. It is a request-response protocol.
* Application Layer Protocol, takes place through TCP/IP
* Default port: 80
* No encryption

# HTTPS
HTTPS - Hyper Text Transfer Protocol Secure, is a protocol used for secure communication over a computer network. It is a secure version of HTTP. It is a request-response protocol.
* Application Layer Protocol, takes place through TCP/IP
* Default port: 443
* Encryption

# Request Multiplexing
Request Multiplexing is a technique used to send multiple requests over a single connection. It is used to reduce the latency and improve the performance of the network.
* Multiple requests are sent over a single connection
* Reduces the latency
* Improves the performance

# HTTP Codes and Error Messages
Success Codes:
100-199: Informational
200-299: Success
300-399: Redirection
400-499: Client Error
500-599: Server Error

# HTTP Methods
- GET: Requests data from a specified resource
- POST: Submits data to be processed to a specified resource
- PUT: Updates a specified resource
- DELETE: Deletes a specified resource
- HEAD: Same as GET but does not return a message body
- CONNECT: Establishes a tunnel to the server identified by a given URI
- OPTIONS: Returns the HTTP methods that the server supports
- TRACE: Performs a message loop-back test along the path to the target resource

# REST APTI
API - Application Programming Interface, is a set of rules and protocols that allows one software application to communicate with another. 

REST - Representational State Transfer, is an architectural style for distributed hypermedia systems. It is a set of constraints that allows the communication between systems. Best for c

Open API - Open Application Programming Interface, is an API that is publicly available for use by developers and other users. It is an API that is available to the public.

Internal API - Internal Application Programming Interface, is an API that is used within the organization. It is an API that is not available to the public.

Composite API - Composite Application Programming Interface, is an API that is composed of multiple APIs. It is an API that is composed of multiple APIs.

Partner API - Partner Application Programming Interface, is an API that is used by the partners of the organization. It is an API that is used by the partners of the organization.

# Same Origin Policy
Same Origin Policy is a security measure used by web browsers to prevent the web pages from making requests to a different domain. It is a security measure that is used to prevent the web pages from making requests to a different domain.

# Cross-Origin Resource Sharing (CORS)
Cross-Origin Resource Sharing is a mechanism that allows the web pages to make requests to a different domain. It is a mechanism that allows the web pages to make requests to a different domain.

# API Architecture Styles
- REST
- SOAP
- RPC
- GraphQL



from flask import Flask

app = Flask(__name__)

@app.route('/users')
def hello_world():
      list = ['John','Ben','Kenny']
      return list

if __name__=='__main__':
      app.run(debug=True)

Consider the above code running on http://127.0.0.1:5000, what is the expected output if we make request to http://127.0.0.1:5000/users?
Group of answer choices

[ "John", "Ben", "Kenny" ]

"John Ben Kenny"

"John", "Ben", "Kenny"

John Ben Kenny

Which of the following is NOT a reason for using CORS (Cross-Origin Resource Sharing)?

Group of answer choices

Allowing servers to control access to their resources

Enabling sharing of resources across different origins

Enhancing website performance

ANS: Enhancing website performance