import socket

host = '203.250.133.88'
port = 11234
BUFF_SIZE = 128

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_address = (host,port)
print("connecting to {} port {}".format(server_address[0],server_address[1]))
sock.connect(server_address)

message = input("Enter File Name : ")
message = bytes(message.encode())

try:
    sock.sendall(message)
    data = sock.recv(BUFF_SIZE)
    if data.decode() == "x":
        print("{}".format(data.decode()))
    else:
        filename = message.decode()
        myFile = open(filename, 'w')
    while True:
        print("{}".format(data.decode()))
        myFile.write(data.decode())
        data = sock.recv(BUFF_SIZE)
except:
    print("예기치 못한 오류")

sock.close()
