# write your code here
# write your code here
import socket
import sys

host, port, message = sys.argv[1:]

with socket.socket() as client:
    client.connect((host, int(port)))
    client.send(message.encode())
    print(client.recv(1024).decode())
