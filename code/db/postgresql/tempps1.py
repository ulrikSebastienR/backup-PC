#https://www.freecodecamp.org/news/if-name-main-python-example/
# original file
#import tempps2
print("file 1's __name__ is set to:{}".format(__name__))

def function_1():
    print("function 1 is executed")

def function_2():
    print("function 2 is executed")

if __name__ == "__main__":
    print("file 1 executed when ran directly")
    function_2()
else:
    print("file 2 executed when imported")

