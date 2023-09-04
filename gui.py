import tkinter as tk
from tkinter import LEFT,BOTTOM,TOP,RIGHT
# name_varibale = tk.StringVar()
window = tk.Tk()
name_label1 = tk.Label(master=window,
                       text ='lable1',
                       )
name_entery1 = tk.Entry(master=window,
                        background= 'pink'
                       )
def click_button() :
    # name_label1['text'] = name_entery1.get()
    name_text = tk.Text()
    name_text.pack()



name_button1 =  tk.Button(master=window,
                          text='click!',
                          command=click_button,
                          activebackground= 'red',
                          background='blue',
                          )

name_label1.grid(row=0,column=0)
name_entery1.grid(row=0,column=1)
name_button1.grid(row=1,column=2)







window.mainloop()