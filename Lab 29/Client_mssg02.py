import socket
import select
import sys
import threading

# Configuration
HOST = '34.123.130.239HH'
PORT = 8888
BUFFER_SIZE = 1024

# Create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server
    client_socket.connect((HOST, PORT))
    print(f"Connected to server at {HOST}:{PORT}")
    print("Enter your username as your first message")
    
    # Function to receive messages from server
    def receive_messages():
        while True:
            try:
                message = client_socket.recv(BUFFER_SIZE)
                if not message:
                    print("Connection to server lost.")
                    sys.exit()
                
                print(message.decode('utf-8'))
            except Exception as e:
                print(f"Error: {e}")
                sys.exit()
    
    # Start thread for receiving messages
    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.daemon = True
    receive_thread.start()
    
    # Main loop for sending messages
    while True:
        message = input()
        if message.lower() == 'exit':
            break
        client_socket.send(message.encode('utf-8'))

except Exception as e:
    print(f"Error: {e}")

finally:
    client_socket.close()
    print("Disconnected from server") 