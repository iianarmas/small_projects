import socket
import threading

# define port and server
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER = 3072
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

# create the socket, pick the type and method
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind socket to address
server.bind(ADDR)


# setup for listening
def handle_client(conn, addr):  # will handle all connections between client and server (individual connection )
    print(f'[NEW CONNECTION] {addr} connected.')

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f'[{addr}] {msg}')

            # send messages
            user = input('[MSG]: ')
            conn.send(user.encode(FORMAT))

        # disconnecting client
    conn.close()


# handle new connections and distribute them to where they need to go
def start():
    server.listen()
    print(f'[LISTENING] Server is listening on {SERVER}')

    # continuous connection running
    while True:
        conn, addr = server.accept()
        addr_name = conn.recv(HEADER).decode(FORMAT)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS]:: [{addr_name}]:: {threading.active_count() - 1}')


print('[STARTING] server is starting...')
start()
