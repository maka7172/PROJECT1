from myproject.errorclass1 import MyClassError
def num_chack (num) :
    if num <0 :
        raise MyClassError ("your number is lower than ziro",num)
    else :
        print ("your number is goood")


try :
    num = int(input("enter your number")) 
    num_chack(num)
except MyClassError as e1 :
    print(e1.message,e1.num)







