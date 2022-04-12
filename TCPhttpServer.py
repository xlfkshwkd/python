#!/usr/bin/python3

import socket

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
    print("echo request from {} port{}".format(address[0], address[1]))
    message = data_sock.recv(BUFF_SIZE)

    if message:
        request = "HTTP/1.0 200 OK\r\n" \
                  "Content-Type: text/html\r\n\r\n" \
                  "<HTML><BODY><H1> Hello, World! </H1>"\
                  "/BODY></HTML>"
        data_sock.sendall(request.encode())
    data_sock.close()
