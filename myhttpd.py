#!/usr/bin/python3
import socket
import sys
import os
import signal
import errno
import subprocess
from urllib.parse import urlparse

phrase = {'200': 'OK', '404': 'File Not Found',
          '500': 'Internal Server Error', '501': 'Not Implemented'}


def shutdownServer(signum, frame):
    print("server shutdown ...")
    sys.exit(0)


def collectZombie(signum, frame):
    while True:
        try:
            pid, status = os.waitpid(-1, os.WNOHANG)
            if pid == 0:
                break
        except:
            break


def getFile(fileName):
    try:
        reqFile = open(fileName, 'r')
        code = '200'
        body = reqFile.read()
    except FileNotFoundError as e:
        code = '404'
        body = '<HTML><HEAD><link rel="short icon" href="#"></HEAD>' \
               '<BODY><H1>404 File Not Found</H1></BODY></HTML>'
    return (code, body)


def doCGI(cgiProg, qString):
    envCGI = dict(os.environ, QUERY_STRING=qString)
    prog = './' + cgiProg
    print(prog)
    try:
        proc = subprocess.Popen([prog], env=envCGI, stdout=subprocess.PIPE)
        code = '200'
        body = proc.communicate()[0].decode()  # pipe byte stream -> unicode
    except Exception as e:
        code = '500'
        body = '<HTML><HEAD><link rel="short icon" href="#"></HEAD>' \
               '<BODY><H1>500 Internal Sever Error</H1></BODY></HTML>'
        pass
    return (code, body)


def doPOSTCGI(cgiProg, qString):
    prog = './' + cgiProg
    print(prog)
    try:
        proc = subprocess.Popen([prog], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        code = '200'
        body = proc.communicate(qString.encode())[0].decode()  # pipe byte stream -> unicode
    except Exception as e:
        code = '500'
        body = '<HTML><HEAD><link rel="short icon" href="#"></HEAD>' \
               '<BODY><H1>500 Internal Sever Error</H1></BODY></HTML>'
        pass
    return (code, body)


def doHTTPService(sock):
    try:
        reqMessage = sock.recv(RECV_BUFF)
    except ConnectionResetError as e:
        sock.close()
        return

    if reqMessage:
        msgString = bytes.decode(reqMessage)
        print(msgString)
        lines = msgString.split('\r\n')
        reqLine = lines[0]
        fields = reqLine.split(' ')
        method = fields[0]
        reqURL = fields[1]
        POSTQ = lines[-1]

        # ver = fields[2]
        # print('requested URL: {}'.format(reqURL))
    else:  # client closed the connection
        sock.close()
        return

    if method == 'GET':
        r = urlparse(reqURL)
        if r.path == '/':
            fileName = 'index.html'
        else:
            fileName = r.path[1:]

        fileType = fileName.split('.')[1]
        if fileType.lower() == 'cgi':  # process CGI
            code, responseBody = doCGI(fileName, r.query)
        else:  # read the requested file
            code, responseBody = getFile(fileName)

    elif method == 'POST':
        r = urlparse(reqURL)
        if r.path == '/':
            fileName = 'index.html'
        else:
            fileName = r.path[1:]

        try:
            fileType = fileName.split('.')[1]
            if fileType.lower() == 'cgi':  # process CGI
                code, responseBody = doPOSTCGI(fileName, POSTQ)
            else:  # read the requested file
                code, responseBody = getFile(fileName)
        except Exception as e:
            code, responseBody = getFile(fileName)

    # elif method == 'POST':
    else:
        code = '501'
        responseBody = '<HTML><HEAD><link rel="short icon" href="#"></HEAD>' \
                       '<BODY><H1>501 Method Not Implemented</H1></BODY></HTML>'

    statusLine = f'HTTP/1.1 {code} {phrase[code]}\r\n'
    headerLine1 = 'Server: vshttpd 0.1\r\n'
    headerLine2 = 'Connection: close\r\n'
    headerLine3 = f'Contents Length: {len(responseBody)}bytes\r\n\r\n'
    # print(len(responseBody))
    sock.sendall(statusLine.encode())
    sock.sendall(headerLine1.encode())
    sock.sendall(headerLine2.encode())
    sock.sendall(headerLine3.encode())
    sock.sendall(responseBody.encode())

    sock.close()


HOST_IP = '203.250.133.88'
# PORT = 18089
# HOST_IP = sys.argv[1]
PORT = int(sys.argv[1])
BACKLOG = 5
RECV_BUFF = 10000

signal.signal(signal.SIGINT, shutdownServer)
signal.signal(signal.SIGCHLD, collectZombie)

try:
    connSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
    print("failed to create a socket")
    sys.exit(1)

try:  # user provided port may be unavaivable
    connSock.bind((HOST_IP, PORT))
except Exception as e:
    print("failed to acquire sockets for port {}".format(PORT))
    sys.exit(1)

print("server running on port {}".format(PORT))
print("press Ctrl+C (or $kill -2 pid) to shutdown the server")

connSock.listen(BACKLOG)

while True:
    print("waiting a new connection...")
    try:
        dataSock, addr = connSock.accept()
        print("got a connection request from: {}".format(addr))
    except IOError as e:
        code, msg = e.args
        if code == errno.EINTR:
            continue
        else:
            raise

    pid = os.fork()
    if pid == 0:
        doHTTPService(dataSock)
        sys.exit(0)

    dataSock.close()
