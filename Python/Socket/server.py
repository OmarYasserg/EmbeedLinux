import socket

HOST = '192.168.1.6'
PORT = 5556
#Communicating Over TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST , PORT))
server.listen(5)

while True:
    print(f"waiting for a device to connect")
    com_socket , address = server.accept()
    print(f"{address} has connected")
    message = com_socket.recv(1023).decode("utf-8")
    print(f"Message is {message}")
    com_socket.send("Got yours thanks".encode("utf-8"))
    com_socket.close()
    print(f"Communication with{address} is ended")