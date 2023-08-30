import socket

HOST = '192.168.1.6'
PORT = 5556

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST , PORT))
client.send(f"Hello from client Two\n".encode("utf-8"))
msg = client.recv(1023)
print(f"msg from {HOST}")
