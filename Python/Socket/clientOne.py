import socket

PORT = 5556
HOST = '192.168.1.6'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.send("Hello from client One \n".encode("utf-8"))
print(f"Connected to server {HOST}")
recMsg = client.recv(1023).decode("utf-8")
print(f"Rec msg is {recMsg}")