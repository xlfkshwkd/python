import tkinter
import tkinter.messagebox

top = tkinter.Tk()
expression = ""

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def bt_clear():
    global expression
    expression = ""
    input_text.set("")

def bt_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

input_frame = tkinter.Frame(top,width=300,height=50)
input_frame.pack(side=tkinter.TOP)  # 위에플레임 생성

input_text = tkinter.StringVar()
input_text.set('')

input_field = tkinter.Entry(input_frame,textvariable=input_text,width=50,justify=tkinter.RIGHT)
input_field.grid(row=0,column=0)
input_field.pack(ipady=10)

btns_frame = tkinter.Frame(top)
btns_frame.pack()
# line 1
clear = tkinter.Button(btns_frame,text="Clear",width=34,height=3,command=bt_clear)
clear.grid(row=0,column=0,columnspan=3)
divide = tkinter.Button(btns_frame,text="/",width=10,height=3,command=lambda :btn_click("/"))
divide.grid(row=0,column=3)
# line 2
seven = tkinter.Button(btns_frame,text="7",width=10,height=3,command=lambda :btn_click("7"))
seven.grid(row=1,column=0)
eight = tkinter.Button(btns_frame,text="8",width=10,height=3,command=lambda :btn_click("8"))
eight.grid(row=1,column=1)
nine = tkinter.Button(btns_frame,text="9",width=10,height=3,command=lambda :btn_click("9"))
nine.grid(row=1,column=2)
multi = tkinter.Button(btns_frame,text="*",width=10,height=3,command=lambda :btn_click("*"))
multi.grid(row=1,column=3)
# line 3
four = tkinter.Button(btns_frame,text="4",width=10,height=3,command=lambda :btn_click("4"))
four.grid(row=2,column=0)
five = tkinter.Button(btns_frame,text="5",width=10,height=3,command=lambda :btn_click("5"))
five.grid(row=2,column=1)
six = tkinter.Button(btns_frame,text="6",width=10,height=3,command=lambda :btn_click("6"))
six.grid(row=2,column=2)
minus = tkinter.Button(btns_frame,text="-",width=10,height=3,command=lambda :btn_click("-"))
minus.grid(row=2,column=3)
# line 4
one = tkinter.Button(btns_frame,text="1",width=10,height=3,command=lambda :btn_click("1"))
one.grid(row=3,column=0)
two = tkinter.Button(btns_frame,text="2",width=10,height=3,command=lambda :btn_click("2"))
two.grid(row=3,column=1)
three = tkinter.Button(btns_frame,text="3",width=10,height=3,command=lambda :btn_click("3"))
three.grid(row=3,column=2)
plus = tkinter.Button(btns_frame,text="+",width=10,height=3,command=lambda :btn_click("+"))
plus.grid(row=3,column=3)
# line 5
zero = tkinter.Button(btns_frame,text="0",width=22,height=3,command=lambda :btn_click("0"))
zero.grid(row=4,column=0,columnspan=2)
point = tkinter.Button(btns_frame,text=".",width=10,height=3,command=lambda :btn_click("."))
point.grid(row=4,column=2)
equals = tkinter.Button(btns_frame,text="=",width=10,height=3,command=lambda :bt_equal())
equals.grid(row=4,column=3)

top.mainloop()