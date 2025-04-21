import socket
s = socket.socket()
server_ip_address = '129.113.155.215'
s.connect((server_ip_address, 12345))

msg = "Hello, Dr. Kim. This is Nick De Leon."
s.send(msg.encode())
print(s.recv(1024))
s.close()