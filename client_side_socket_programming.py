import socket

PORT = 5050
SERVER = '127.0.1.1'
HEADER = 3072
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)


# sendng messages
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(HEADER).decode(FORMAT))


name = input('Enter name: ')
client.send(bytes(name, FORMAT))

while True:
    user = input('[MSG]: ')
    if user != DISCONNECT_MESSAGE:
        send(user)
    else:
        break

