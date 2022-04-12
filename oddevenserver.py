#!/usr/bin/python3
import socket

host = ''
port = 10124
BUFF_SIZE = 128

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = (host, port)
sock.bind(server_address)

while True:
    print(" waiting for request...")
    message, client_address = sock.recvfrom(BUFF_SIZE)

    print("echo requset from {} port{}". format(client_address[0], client_address[1]))
    try:
        if int(message.decode())%2 == 0:
            print("Even number")
        else:
            print("odd number ")
    except:
        print("no number")

    sock.sendto(message, client_address)

sock.close()
