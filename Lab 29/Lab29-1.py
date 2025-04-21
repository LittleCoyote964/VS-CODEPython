import socket

s = socket.socket()

s.bind(("129.113.81.217", 12345))
s.listen()

while True:
    c, addr = s.accept() #used to establish connection with the client
    print("Got connection from", addr)
    client_msg = c.recv(1024)
    print("Received: " + client_msg.decode())
    server_msg = "Testing server"
    c.send(server_msg.encode())
    c.close()