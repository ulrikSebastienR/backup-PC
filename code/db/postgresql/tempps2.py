# file where I make import
import tempps1
print("file 2's __name__ is:{}".format(__name__))

def function_3():
    print("function 3 is executed")

if __name__ == "__main__":
    print("file 2 executed when ran directly")
    function_3()
else:
    print("file 1 executed when imported")
    function_1()
    function_2()