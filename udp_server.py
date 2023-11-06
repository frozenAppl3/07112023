import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 12345)
server_socket.bind(server_address)

print("Server is listening on {}:{}".format(*server_address))

while True:
	data, client_address = server_socket.recvfrom(1025)
	print("Received data from {}:{}".format(*client_address))
	print("Data received: {}".format(data.decode()))

	response = "Hello, client!"
	server_socket.sendto(response.encode(), client_address)

