class MyClassError(Exception) :
    def __init__(self,message,num) :
        self.message = message
        self.num = num 
