import threading
import socket

# Server configuration
host = '127.0.0.1' # Localhost (use LAN IP to allow external connections)
port = 55556 # Arbitrary non-privileged port

# Create a TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server.bind((host, port))

# Put the server into listening mode
server.listen()

# Lists to keep track of connected clients and their nicknames
clients = []
nicknames = []

# Send a message to all connected clients. This function is called whenever a client sends a message.
def broadcast(message):
    for client in clients:
        client.send(message)

#   Handle communication with a single client. Runs in its own thread so multiple clients can be handled concurrently.
def handle(client):
    while True:
        try:
            # Receive a message from the client
            message = client.recv(1024)

            # Broadcast the received message to all clients
            broadcast(message)
        except:
             # If an error occurs (client disconnects, etc.)
            index = clients.index(client)
            clients.remove(client)
            client.close()

             # Remove and announce the disconnected client
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('ascii'))
            nicknames.remove(nickname)
            break

#  Main server loop. Accepts new client connections and starts a thread for each one.
def receive():
    while True:
        # Accept a new client connection
        client, address = server.accept()
        print(f'Connected with {str(address)}')
        
        # Ask the client for a nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        # Store client and nickname
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}.')
        broadcast(f'{nickname} joined the chat!'.encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))

        # Start a new thread to handle this client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print('Server is listening...')
receive()


