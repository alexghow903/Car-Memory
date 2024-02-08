import socket

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind(("50:13:1d:5f:78:a2", 4))
server.listen(1)

client, addr = server.accept()

try:
    while True:
        data = client.recv()