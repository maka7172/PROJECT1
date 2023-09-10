import tkinter as tk
from tkinter import ttk
import os
window = tk.Tk()
window.title('calc1')
os.system('cls')
num = {'num1' : '','num2' : '','op' : ''}
key_list_dic = [{'text' : 7,'command' : lambda : print_result(7)},
                {'text' : 8,'command' : lambda : print_result(8)},
                {'text' : 9,'command' : lambda : print_result(9)},
                {'text' : '*','command' : lambda : print_result('*')},
                {'text' : 4,'command' : lambda : print_result(4)},
                {'text' : 5,'command' : lambda : print_result(5)},
                {'text' : 6,'command' : lambda : print_result(6)},
                {'text' : '/','command' : lambda : print_result('/')},
                {'text' : 1,'command' : lambda : print_result(1)},
                {'text' : 2,'command' : lambda : print_result(2)},
                {'text' : 3,'command' : lambda : print_result(3)},
                {'text' : '+','command' : lambda : print_result('+')},
                {'text' : 0,'command' : lambda : print_result(0)},
                {'text' : 'c','command' : lambda : print_result('c')},
                {'text' : '.','command' : lambda : print_result('.')},
                {'text' : '-','command' : lambda : print_result('-')},
                ]

def calc_show (char) :
    """return all of opration """
    lbl_show['text'] += str(char) 
 
def calc () :
    """return calc opration"""
    if num['op'] == '*' :
        return num['num1'] * num['num2']
    elif num['op'] == '/' :
        return num['num1'] / num['num2']
    elif num['op'] == '+' :
        return num['num1'] + num['num2']
    elif num['op'] == '-' :
        return num['num1'] - num['num2']

def print_result(char) :
    current = lbl_result['text']
    
    if char == '.' :
        for i  in current :
            if i == '.' :
                char =''
       
    calc_show(char)
    if char not in ['*','/','+','-','c','='] :
        if num['op'] == '' :#creat num1
            lbl_result['text'] += str(char)
        elif num['op'] != '' and num['num1'] != '' : #creat num2
            lbl_result['text'] += str(char)
        else : #renew calc oprator
            lbl_result['text'] = ''
            for i in num.keys() :
                num[i] = ''
            lbl_result['text'] += str(char)
    elif char == 'c' : #clear all 
        lbl_result['text'] = ""
        lbl_show['text'] = ""
        for i in num.keys() :
                num[i] = ''
    elif char in ['*','/','+','-']  : #enter opration 
        if lbl_result['text'] != '' :
            if num['num1'] != '' : # when user dont enter = and use other opration
                num['num2'] = float(lbl_result['text'])
                num['num1'] = calc()
                lbl_result['text'] = ""
                num['op'] = char
            else : # when num1 is empty and user enter operation  
                num['num1'] = float(lbl_result['text'])
                num['op'] = char
                lbl_result['text'] = ""
    elif char == '=' : #when user enter equ =
        if lbl_result['text'] != '':
            num['num2'] = float(lbl_result['text'])
            lbl_result['text'] = calc()
            num['num1'] = ''
            num['num2'] = ''
            lbl_show ['text'] = ""
lbl_show = tk.Label(window,
                       width=45,
                       height=2)
lbl_show.grid(row=0,
                column=0,
                columnspan=4,
                )    
lbl_result = tk.Label(window,
                       width=45,
                       height=2)
lbl_result.grid(row=1,
                column=0,
                columnspan=4,
                )

btn_equ = ttk.Button(window,
                    text= '=',
                    command= lambda : print_result('='),
                    width=40
                    )
btn_equ.grid(row=6,column=0,columnspan=4)


#creat buttons
for i , char in enumerate  (key_list_dic) :
   
    btn = ttk.Button(window,
                          text=char['text'],
                          command= char['command'],
                            )
    btn.grid(row=i//4 + 2,column=i%4)





window.mainloop()
