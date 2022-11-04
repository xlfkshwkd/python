import tkinter
import tkinter.messagebox


input_text = StringVar()
input_field = Entry(input_frame, textvariable=input_text, width=50, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)


btns_frame = Frame(top)
btns_frame.pack()
# line 1
clear = Button(btns_frame, text="Clear", width=34, height=3,command= bt_clear())
clear.grid(row=0, column=0, columnspan=3)
divide = Button(btns_frame, text="/", width=10, height=3,command=lambda: btn_click("/"))
divide.grid(row=0, column=3)







# line 5
zero = Button(btns_frame, text="0", width=22, height=3,
command=lambda: btn_click(0))
zero.grid(row=4, column=0, columnspan=2)
point = Button(btns_frame, text=".",width=10, height=3,
command=lambda: btn_click("."))
point.grid(row=4, column=2)
equals = Button(btns_frame, text="=", width=10, height=3,
command=lambda: bt_equal())
equals.grid(row=4, column=3)
