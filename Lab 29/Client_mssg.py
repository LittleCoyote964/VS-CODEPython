import socket
s = socket.socket()
server_ip_address = '127.0.0.1'
s.connect((server_ip_address, 8888))

msg = "Hello. This is Nick De Leon."
s.send(msg.encode())
print(s.recv(1024))
s.close()