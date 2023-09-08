import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('calc1')
lbl_persenteg = ttk.Label(master= window ,
                         text= 'persantege',
                         )
btn_daytools =  ttk.Button(master=window,
                          text='DAYTOOLS',
                          )
btn_timer = ttk.Button(master=window,
                      text='TIMER',
                      )
ent_show = ttk.Entry(master=window,
                    width=49)
btn_ac = ttk.Button(master=window,
                   text='AC' ,
                   )
btn_plus_mines = ttk.Button(master=window,
                           text='+/-',
                           )
btn_persentege = ttk.Button(master=window,
                           text='%',
                           )
btn_div =ttk.Button(master=window,
                   text='/',
                   )
btn_multi =ttk.Button(master=window,
                   text='*',
                   )
btn_plus =ttk.Button(master=window,
                   text='+',
                   )
btn_min =ttk.Button(master=window,
                   text='-',
                   )
btn_equ =ttk.Button(master=window,
                   text='=',
                   )
btn_auditor =ttk.Button(master=window,
                   text=',',
                   )
btn_number_0 = ttk.Button(master=window,
                         text='0',
                         width=23,
                         )
btn_number_1 = ttk.Button(master=window,
                         text='1',
                         )
btn_number_2 = ttk.Button(master=window,
                         text='2',
                         )
btn_number_3 = ttk.Button(master=window,
                         text='3',
                         )
btn_number_4 = ttk.Button(master=window,
                         text='4',
                         )
btn_number_5 = ttk.Button(master=window,
                         text='5',
                         )
btn_number_6 = ttk.Button(master=window,
                         text='6',
                         )
btn_number_7 = ttk.Button(master=window,
                         text='7',
                         )
btn_number_8 = ttk.Button(master=window,
                         text='8',
                         )
btn_number_9 = ttk.Button(master=window,
                         text='9',
                         )

lbl_persenteg.grid(row=0,column=0)
btn_daytools.grid(row=1,column=0)
btn_timer.grid(row=1,column=1)
ent_show.grid(row=2,column=0,columnspan=4,padx=(2))
btn_ac.grid(row=3,column=0)
btn_plus_mines.grid(row=3,column=1)
btn_persentege.grid(row=3,column=2)
btn_div.grid(row=3,column=3)
btn_number_7.grid(row=4,column=0)
btn_number_8.grid(row=4,column=1)
btn_number_9.grid(row=4,column=2)
btn_multi.grid(row=4,column=3)
btn_number_4.grid(row=5,column=0)
btn_number_5.grid(row=5,column=1)
btn_number_6.grid(row=5,column=2)
btn_min.grid(row=5,column=3)
btn_number_1.grid(row=6,column=0)
btn_number_2.grid(row=6,column=1)
btn_number_3.grid(row=6,column=2)
btn_plus.grid(row=6,column=3)
btn_number_0.grid(row=7,column=0,columnspan=2)
btn_auditor.grid(row=7,column=2)
btn_equ.grid(row=7,column=3)
















window.mainloop()
