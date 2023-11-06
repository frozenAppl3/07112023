import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'  
port = 12345  
server_socket.bind((host, port))

server_socket.listen(5)

print(f"Server is listening on {host}:{port}")

while True:
	client_socket, client_address = server_socket.accept()

	print(f"Connected to {client_address}")

	while True:
		data = client_socket.recv(1024)
		print(data)
		if not data:
			break
		client_socket.send(data)

	client_socket.close()

	server_socket.close()
