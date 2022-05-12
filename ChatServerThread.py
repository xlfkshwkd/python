#!/usr/bin/python3
import socket
import threading

host = ''
port = 12334
BUFSIZ = 1024
connections = {}


def init_chat(sock):
    try:
        sock.send("***Hello! I am Server. Please send me your nickname***".encode())
        name = sock.recv(BUFSIZ).decode()
        welcome = "Welocome {}. If want to quit, send me 'Bye!'".format(name)
        sock.send(welcome.encode())
        message = "{} has joined...".format(name)
        broadcast(message.encode())
        # connections{client_sock: name} key=client_sock, value=name item=key:value
        connections[sock] = name
        relay_message(sock, name)
    except:
        pass
    return


def relay_message(sockfd, sender_name):
    while True:
        try:
            message = sockfd.recv(BUFSIZ)
        except ConnectionResetError:
            break

        if message.decode() != "Bye!":
            broadcast(message, sender_name)
        else:
            sockfd.close()
            del connections[sockfd]
            broadcast("{} has left... ".format(sender_name).encode())
            break
    return


def broadcast(msg, nickname=''):
    # Broadcasts a message to all the clients.
    if not nickname:
        nickname = "Server"
    # dictionary dict.keys(), dict.values(), dict.items: default is keys()
    for sock in connections:
        message = nickname + '> ' + msg.decode()
        sock.sendall(message.encode())
    return


conn_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn_sock.bind((host, port))
conn_sock.listen(5)

while True:
    print("Waiting for connection...")
    data_sock, client_addr = conn_sock.accept()
    print("Client from {} has connected...".format(client_addr[0]))

    client_thread = threading.Thread(target=init_chat, args=(data_sock,))
    client_thread.daemon = True
    client_thread.start()