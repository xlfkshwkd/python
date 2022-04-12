#!/usr/bin/python3

import socket
import sys

host = ''
port = 11234
BUFF_SIZE = 128
BACKLOG = 5
conn_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (host, port)
conn_sock.bind(server_address)

conn_sock.listen(BACKLOG)

while True:
    print("waiting for requests..")
    data_sock, address = conn_sock.accept()
    print("echo request from {} port {}".format(address[0], address[1]))
    message = data_sock.recv(BUFF_SIZE)
    print("recevied message : %s\n " % message.decode())

    if message:
        myFile = message.decode()
        try:
            filename = open(myFile, 'r')
        except FileNotFoundError:
            data_sock.sendall("x".encode())
            print("x")
            data_sock.close()
            sys.exit()

        for line in myFile:
            data_sock.sendall(line.encode())

myfile.close()
data_sock.close()
