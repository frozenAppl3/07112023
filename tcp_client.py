import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_host = 'localhost'  # Change to the server's host
server_port = 12345  # Change to the server's port
client_socket.connect((server_host, server_port))

while True:
	message = input("Enter a message (or 'exit' to quit): ")
	if message.lower() == 'exit':
		break

	client_socket.send(message.encode())

	data = client_socket.recv(1024)
	print(f"Server says: {data.decode()}")

client_socket.close()
