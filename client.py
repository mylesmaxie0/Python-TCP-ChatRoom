import socket
import threading

# Prompt the user for a nickname
nickname = input("Choose your nickname: ")

# Create a TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect(('127.0.0.1', 55556))

# Continuously listen for messages from the server. Runs in its own thread so receiving does not block user input.
def receive():
    while True:
        try:
            # Receive message from the server
            message = client.recv(1024).decode('ascii')

            # Server requests nickname during initial handshake
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
                pass
            else:
                print(message)
        except:
            # If an error occurs, close the connection
            print("An error occurred! Disconnecting from server.")
            client.close()
            break

# Continuously read user input and send messages to the server. Runs in its own thread so sending does not block receiving.
def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

# Start receiving thread
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# Start writing thread
write_thread = threading.Thread(target=write)
write_thread.start()



