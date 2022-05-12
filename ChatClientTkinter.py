#!/usr/bin/python3

import socket
import threading
import tkinter

BUFSIZ = 1024
host = '203.250.133.88'
port = 10020

def recv_message(sock):
    while True:
        try:
            message = sock.recv(BUFSIZ).decode()
            message_box.insert(tkinter.END, message)
            message_box.yview(tkinter.END)
        except :
            break

def send_message(event=None):
    message = input_text.get()
    input_text.set("")
    sock.sendall(message.encode())
    if message == "Bye!":
        sock.close()
        top.destroy()

def on_closing(event=None):
    input_text.set("Bye!")
    send_message()

# top 윈도우
top = tkinter.Tk()
top.title("Chat Box")
top.protocol("WM_DELETE_WINDOW", on_closing)

# 메시지 리스트박스 + 스크롤바 in 프레임
frame = tkinter.Frame(top)
scrollbar = tkinter.Scrollbar(frame)
message_box = tkinter.Listbox(frame, height=15, width=50)

# enable scrollbar dragging
scrollbar.configure(command = message_box.yview)
message_box.configure(yscrollcommand = scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
message_box.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
frame.pack()

# StringVar는 메시지를 입력하는 entry 위젯과 연결됨.
# 변수의 스트링이 위젯에 나타나고 위젯에 입력된 스트링이 변수에 저장됨
input_text = tkinter.StringVar()
input_text.set("")

text_field = tkinter.Entry(top, textvariable=input_text)
text_field.bind("<Return>", send_message)
text_field.pack()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

recv_thread = threading.Thread(target=recv_message, args=(sock, ))
recv_thread.start()

tkinter.mainloop()