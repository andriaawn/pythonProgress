# global variable
x = 10
# function definition 
def foo():  # function definition
    print(x)    # print global variable x

foo() # 10


def number():
    x = 20
    print(x) # 20

number()

print(x) # 10

# different global varibale and local variable, global variable outside the function and local variable inside the function

fruit = 'apple'

def fruits():
    fruit = 'banana'
    print(fruit) # banana

fruits() # banana

print("fruit outside the function", fruit) # apple

# why we use global variable
# global variable is used to store the data which is used by multiple functions

# why we use local variable
# local variable is used to store the data which is used by
# only one function

# how to change the global variable value inside the function
# using global keyword
def change():
    global fruit    # global fruit is ? apple
    fruit = 'mango'
    print(fruit)

change() # mango    

x = 'awesome'
def myfunc():
  global x
  x = 'fantastic'
myfunc()
print('Python is ' + x) # Python is fantastic ? why ? because we change the value of x using global keyword inside the function

# but the myfunc() is not called on print statement, so how it is possible ? 
# because the function is called before the print statement
# good

