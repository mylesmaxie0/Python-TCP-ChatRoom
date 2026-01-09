# Secure TCP Chat Room

## Overview

The Secure TCP Chat Room is a Python-based client-server application that enables encrypted and confidential communication between multiple users over TCP. The project demonstrates practical knowledge of networking fundamentals, secure communication concepts, and socket programming.


### Features
- Encrypted messaging to ensure confidentiality
- TCP-based client-server architecture
- Support for multiple concurrent users
- Reliable message delivery using TCP sockets
- Clear separation of client and server logic

### Technologies Used
- Python
- TCP Sockets
- Networking Protocols
- Encryption Techniques (e.g., symmetric or asymmetric encryption, depending on implementation)

### Architecture

The application follows a traditional TCP client-server model:
- The server listens for incoming client connections and manages message routing.
- Each client establishes a TCP connection to the server and securely sends and receives messages.
- Encryption is applied before transmission and decrypted upon receipt to protect data in transit.

### Usage 

#### Start the Server
```bash
python3 server.py
```
The server will:
- Bind to a specified IP address and port
- Listen for incoming client connections
- Handle encrypted message distribution between clients


#### Start a Client
```bash
python3 client.py
```
When prompted:
- Enter the server’s IP address and port
- Choose a username (if supported)

Chat Functionality
- Messages typed by a client are encrypted before being sent
- The server relays messages to connected clients
- Received messages are decrypted and displayed in the terminal


### Learning Outcomes

This project demonstrates:
- Strong understanding of TCP/IP networking concepts
- Practical experience with Python socket programming
- Awareness of secure communication principles

