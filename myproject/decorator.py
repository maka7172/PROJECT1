def my_decorator(input_func) :
    def wrapper() :
        for i in range (5) :
            input_func()
    return wrapper