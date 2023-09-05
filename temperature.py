import tkinter as tk
from tkinter import TOP,BOTTOM,RIGHT

window1 = tk.Tk()
window1.title('Conver Temperature')
farenhait_label = tk.Label(master=window1,
                           height=3,
                           font="TOHOMA",
                           text= 'farenhait : ',
                            )
entery_give_faren = tk.Entry(master=window1,
                             width=50,
                             )
# num = float(input("enter your number")) # you can give data from rozberipy
# entery_give_faren.insert(0,num)

celsus_label = tk.Label(master=window1,
                        text='celsus')
result_label = tk.Label(master=window1,
                        text='result will be here',
                        )
def calc_far_to_cel() :
    result_label['text'] = f"the result is :{(float(entery_give_faren.get())-32)*5.9 }"

button_calc = tk.Button(master=window1,
                        text='calc!!',
                        command=calc_far_to_cel,
                        )
    
farenhait_label.grid(row=0,column=0)
entery_give_faren.grid(row=0,column=1,sticky=('W',))
button_calc.grid(row=0,column=2,sticky=("w",))
celsus_label.grid(row=2,column=0)
result_label.grid(row=2,column=1,columnspan=2)
    
window1.mainloop()
