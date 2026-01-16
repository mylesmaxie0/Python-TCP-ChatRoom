# Import libraries for networking and multi-threading
import socket
import threading

# Import RSA encryption library
import rsa

# Generate a 1024-bit RSA key pair for this client
public_key, private_key = rsa.newkeys(1024)
# Public key of the remote peer (to be received during handshake)
public_Stranger = None


# Ask user to choose between hosting or joining
choice = input("Do you want to Host (1) or Join (2) a chat? ")

if choice == '1':
    # Host mode: create server socket and wait for connection
    server = socket .socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("<HOST_IP>", 9999))
    server.listen(1)

    # Accept incoming connection
    client, _ = server.accept()
    # Send our public key to the remote peer
    client.send(public_key.save_pkcs1("PEM"))
    # Receive and store the remote peer's public key
    public_Stranger = rsa.PublicKey.load_pkcs1(client.recv(1024))
elif choice == '2':
    # Join mode: connect to host
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("192.168.1.238", 9999))
    # Receive and store the remote peer's public key first
    public_Stranger = rsa.PublicKey.load_pkcs1(client.recv(1024))
    # Send our public key
    client.send(public_key.save_pkcs1("PEM"))
else:
    # Invalid choice, exit
    exit()

# Thread function to send encrypted messages
def send_messages(c):
    while True:
        # Get message from user input
        message = input("")
        # Encrypt message with peer's public key and send
        c.send(rsa.encrypt(message.encode(), public_Stranger))
        # Uncomment the line below and comment the line above to disable encryption
        # c.send(message.encode())
        # Display sent message to user
        print("You: " + message)


# Thread function to receive and decrypt messages
def receive_messages(c):
    while True:
        # Receive encrypted message, decrypt with our private key, and display
        print("Stranger: " + rsa.decrypt(c.recv(1024), private_key).decode())
      # Uncomment the line below and comment the line above to disable encryption
      # print("Stranger: " + c.recv(1024).decode())



# Start send and receive threads to handle messages concurrently
threading.Thread(target=send_messages, args=(client,)).start()
threading.Thread(target=receive_messages, args=(client,)).start()

