import tkinter as tk
window = tk.Tk()
def my_input () :
    name_lable=tk.Label(master=window,name_lable="enter your name :")
    name = tk.Entry(master= window)

    # input("enter name :   ")
    number_lable = tk.Label(master=window,number_lable="enter number :")
    number = tk.Entry(master=window)
    # int(input("enter number of name :   "))
    name_lable.pack()
    name.pack()
    number_lable.pack()
    number.pack()
    
    return name ,number

def my_dic (file_name) :
    list_name = {}
    with open(file_name , 'r') as reading :
        my_list_grate = (reading.read().split("\n"))
    for item in my_list_grate :
        i = item.split(' ')
        list_name[i[0]] = int(i[1])
    print(list_name)
    return list_name

def my_insert(file_name,name,number) :
    with open(file_name,'a') as append :
        append.write(f'\n{name} {number}')
while True :
    mydic = my_dic('txt&word\grate.txt')
    
    for i in mydic.items() :
        # print(f"in coeiz {i[0]}\'s number is  : {i[1]}")
        text = tk.Label(text=f"in coeiz {i[0]}\'s number is  : {i[1]}")
        text.pack()
        

    qustion = input("do you like append a new item ? (y or n) :  ")
    if qustion == 'y' :
        while True :
            try :
                name,number = my_input()
                my_insert('txt&word\grate.txt',name ,number)
                break
            except ValueError :
                print("your enter number is invalid")
            
    elif qustion == 'n' :
        print('thanks for select we !!!')
        break
window.mainloop()
