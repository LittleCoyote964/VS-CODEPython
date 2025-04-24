import socket
import select
import sys

# Configuration
HOST = '0.0.0.0'
PORT = 8888
BUFFER_SIZE = 1024

# Dictionary to store client connections and usernames
clients = {}

# Create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(100)

print(f"Server started on {HOST}:{PORT}, welcome to Nick's server")

# List of sockets to monitor
sockets_list = [server_socket]

def broadcast(message, sender_socket):
    """Send a message to all connected clients except the sender"""
    for client_socket in clients:
        if client_socket != sender_socket:
            try:
                client_socket.send(message)
            except:
                # If connection is broken, close and remove the client
                client_socket.close()
                sockets_list.remove(client_socket)
                del clients[client_socket]

try:
    while True:
        # Use select to monitor sockets
        read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
        
        for notified_socket in read_sockets:
            # Handle new connection
            if notified_socket == server_socket:
                client_socket, client_address = server_socket.accept()
                sockets_list.append(client_socket)
                print(f"New connection from {client_address[0]}:{client_address[1]}")
                
                # Client is not registered yet (no username)
                clients[client_socket] = None
                
            # Handle message from existing client
            else:
                try:
                    message = notified_socket.recv(BUFFER_SIZE)
                    
                    if not message:
                        # Empty message means client disconnected
                        print(f"Closed connection from {clients[notified_socket]}")
                        sockets_list.remove(notified_socket)
                        del clients[notified_socket]
                        continue
                    
                    message_str = message.decode('utf-8').strip()
                    
                    # If this client doesn't have a username yet, register it
                    if clients[notified_socket] is None:
                        username = message_str.split()[0]
                        clients[notified_socket] = username
                        print(f"User {username} registered")
                        continue
                    
                    # Format message with username and broadcast
                    username = clients[notified_socket]
                    formatted_message = f"{username}: {message_str}".encode('utf-8')
                    print(formatted_message.decode('utf-8'))
                    broadcast(formatted_message, notified_socket)
                    
                except Exception as e:
                    print(f"Error: {e}")
                    if notified_socket in sockets_list:
                        sockets_list.remove(notified_socket)
                    if notified_socket in clients:
                        del clients[notified_socket]
        
        # Handle exception sockets
        for notified_socket in exception_sockets:
            sockets_list.remove(notified_socket)
            if notified_socket in clients:
                del clients[notified_socket]

except KeyboardInterrupt:
    print("Server is shutting down")
    server_socket.close() 
