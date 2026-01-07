# Python TCP Chat Room

## Overview

A lightweight TCP chat room written in Python, demonstrating socket programming and basic client–server communication using the Python standard library.

This project is intended as an educational example of how TCP sockets, threading, and message broadcasting work in a simple client–server architecture.

---

## Features

- TCP client–server architecture
- Multiple concurrent clients using threading
- Real-time message broadcasting
- Nickname-based user identification
- No external dependencies

---

## Project Structure
---

## How It Works

### Server

- Listens on a specified host and port
- Accepts incoming client connections
- Maintains a list of connected clients
- Spawns a thread per client to handle messages
- Broadcasts messages to all connected clients

### Client

- Connects to the server using TCP
- Sends a nickname during the initial handshake
- Uses one thread for sending messages
- Uses another thread for receiving messages
- Displays messages in real time

---

## Requirements

- Python 3.8 or newer
- Python standard library only

---

## Usage

### Start the Server

```bash
python server.py
