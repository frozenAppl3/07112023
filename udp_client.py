import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 12345)
message = "Hello, server!"

client_socket.sendto(message.encode(), server_address)
print("Sent data to {}:{}".format(*server_address))

response, server_address = client_socket.recvfrom(1024)
print("Received response from {}:{}".format(*server_address))
print("Response: {}".format(response.decode()))

client_socket.close()
