import tkinter as tk
from tkinter import TOP,BOTTOM,RIGHT
import string

# def check_page() :
#     if entery_give_faren.get() != True :
#         result_label['text'] = 'the temperature is empty!!'

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


def calc_far_to_cel(*args) :
    ent_input = entery_give_faren.get()
    try :
        ent_value = float(ent_input)
        result_label['text'] = f"the result is :{ent_value}"
    except ValueError :
        if (ent_input) != '' :
            result_label['text'] = "you shuld enter valid data"
        else :
            result_label['text'] = "the input is empty!!"
        
window1.bind('<Return>' , calc_far_to_cel)
button_calc = tk.Button(master=window1,
                        text='calc!!',
                        command=calc_far_to_cel,
                        )
    
farenhait_label.grid(row=0,column=0)
entery_give_faren.grid(row=0,column=1,sticky=('W',))
button_calc.grid(row=0,column=2,sticky=("w",))
celsus_label.grid(row=2,column=0)
result_label.grid(row=2,column=1,columnspan=2)

if entery_give_faren.get() != True :
    result_label['text'] = 'the temperature is empty!!'

window1.mainloop()
