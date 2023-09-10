from myproject.decorator import my_decorator
import os

path = os.getcwd().split('\\')
@my_decorator
def path_path() :
    path = os.getcwd().split('\\')
    print(path)

path_path()
 