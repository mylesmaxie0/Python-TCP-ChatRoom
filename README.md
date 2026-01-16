# Encrypted TCP Chat Room 

## Overview

This project is a simple **encrypted peer-to-peer TCP chat application** written in Python. It allows two users to either **host** or **join** a chat session and exchange messages securely using **RSA public-key encryption**.

The application uses Python’s built-in `socket` and `threading` libraries for networking and concurrency, along with the `rsa` library to encrypt messages in transit.

## Features

* Peer-to-peer TCP chat
* Host or join mode
* RSA public/private key generation
* Encrypted message transmission
* Concurrent send and receive threads
* Minimal dependencies

## Requirements

* Python 3.8+
* `rsa` Python package

Install dependencies:

```bash
pip install rsa
```

## File Structure

```
.
├── main.py        # Chat application
└── README.md      # Project documentation
```

## How It Works

1. Each client generates an RSA public/private key pair at startup.
2. The host opens a TCP socket and waits for an incoming connection.
3. The joining client connects to the host’s IP and port.
4. Public keys are exchanged between peers.
5. Messages are encrypted using the recipient’s public key.
6. Incoming messages are decrypted using the local private key.
7. Separate threads handle sending and receiving messages simultaneously.

## Usage

### 1. Configure Network Settings

In `main.py`, update the following values to match your environment:

```python
server.bind(("<HOST_IP>", 9999))
```

Replace `<HOST_IP>` with the host machine’s local or reachable IP address.

### 2. Run the Program

```bash
python main.py
```

### 3. Choose a Mode

When prompted:

* Enter `1` to **Host** a chat
* Enter `2` to **Join** a chat

### 4. Start Chatting

* Type messages and press Enter to send
* Incoming messages will be decrypted and displayed automatically

## Security Notes

* RSA encryption is used directly for message payloads.
* This implementation is for **educational purposes** and not production-ready.
* Messages are limited by RSA key size (1024 bits).


## Traffic Analysis with Wireshark

This project can be used to demonstrate the difference between **unencrypted** and **encrypted** network traffic using Wireshark.

### Objective

To observe how plaintext messages are visible over the network when no encryption is used, and how RSA encryption obscures message contents during transmission.


### Unencrypted Traffic Observation

If message encryption is temporarily disabled in the code:

* Chat messages appear **in plaintext** within TCP payloads.
* Message contents can be viewed directly via:

  * Packet Details → TCP → Payload
  * Follow → TCP Stream
* This demonstrates how TCP traffic is readable by any intermediary on the network.

#### Unencrypted Traffic Chat
<img width="852" height="709" alt="Screenshot 2026-01-16 at 12 55 57 PM" src="https://github.com/user-attachments/assets/e1f82da8-68b8-462f-abe1-82529e26b0f4" />

#### Wireshark Capture of Chat
- Server (9999) -> Client (52094)
<img width="1728" height="1117" alt="Screenshot 2026-01-16 at 1 09 32 PM" src="https://github.com/user-attachments/assets/dd7880de-3879-4c5b-a734-e37fc53db4bc" />


### Encrypted Traffic Observation

With RSA encryption enabled:

* Packet payloads appear as **random binary data**.
* Message contents are no longer human-readable.
* Following the TCP stream shows encrypted ciphertext rather than plaintext messages.

#### Encrypted Traffic Chat
<img width="858" height="750" alt="Screenshot 2026-01-16 at 1 17 23 PM" src="https://github.com/user-attachments/assets/d4dd1687-c579-4c47-9cbd-d52d503775d2" />

#### Wireshark Capture of Chat
- Client (52186) -> Server (9999)
<img width="1728" height="1086" alt="Screenshot 2026-01-16 at 1 15 49 PM" src="https://github.com/user-attachments/assets/a2e25808-af2a-4d57-bedb-dd56d5ca5dba" />


### Key Takeaways

* TCP provides **no built-in confidentiality**.
* Encryption is essential to protect data from passive network observers.
* Public-key encryption successfully prevents message disclosure even when traffic is captured.

This section reinforces fundamental networking and security concepts, including **packet inspection**, **payload analysis**, and **encryption effectiveness**.

## Disclaimer

This project is intended for **learning and experimentation only**. Do not use it for sensitive or real-world secure communications.


