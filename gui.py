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
name_text = tk.Text() 
name1 =''
def click_button() :
    # name_label1['text'] = name_entery1.get()
    
    name_text.grid(row=4,column=0,columnspan=3)
    name1 = name_text.get('1.0',tk.END)
    
    
def sub_button() :
    name_text.insert('2.0',name_entery1.get()) #entry get() and text insert('1.0',tk.END  or '1.8')
    name_entery1.insert(0,name_text.get('1.0',tk.END)) # entry insert(0,'comments') and text get('1.0',....)

name_button2 =  tk.Button(master=window,
                          text='click!',
                          command=sub_button,
                          activebackground= 'red',
                          background='green',
                          )

name_button1 =  tk.Button(master=window,
                          text='click!',
                          command=click_button,
                          activebackground= 'red',
                          background='blue',
                          )

name_label1.grid(row=0,column=0)
name_entery1.grid(row=0,column=1)
name_button1.grid(row=1,column=2)
name_button2.grid(row=4,column=5)







window.mainloop()