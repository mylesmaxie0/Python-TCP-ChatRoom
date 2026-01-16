# Encrypted TCP Chat Room (Python)

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

#### Unencrypted Traffic

### Encrypted Traffic Observation

With RSA encryption enabled:

* Packet payloads appear as **random binary data**.
* Message contents are no longer human-readable.
* Following the TCP stream shows encrypted ciphertext rather than plaintext messages.


#### Encrypted Traffic

### Key Takeaways

* TCP provides **no built-in confidentiality**.
* Encryption is essential to protect data from passive network observers.
* Public-key encryption successfully prevents message disclosure even when traffic is captured.

This section reinforces fundamental networking and security concepts, including **packet inspection**, **payload analysis**, and **encryption effectiveness**.

## Possible Improvements

* Use hybrid encryption (RSA + AES)
* Add message signing for authenticity
* Support multiple clients
* Implement dynamic IP/port configuration
* Add exception handling and clean disconnects
* Replace blocking sockets with async I/O

## Disclaimer

This project is intended for **learning and experimentation only**. Do not use it for sensitive or real-world secure communications.

## License

MIT License (or specify your preferred license)
