# True or False

print(1 == 1) # True
print(1 != 2 ) # True
print(1 > 2) # False

# etc ... 

# if boolean statements implemented in a program 

# if true: the program will run the code inside the if statemnt 

a = 200 
b = 33
if a > b : 
    print(f"the value of a is {a} greater than b {b}")
else:
    print(f"the value of a is {a} less than b {b}")


# evaluating boolean expressions

x = "hello dear"
y = 10


print(bool(x)) # True
print(bool(y)) # True
print(bool("")) # False
print(bool(0)) # False


# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.

# Any number is True, except 0.

# Any list, tuple, set, and dictionary are True, except empty ones.


# function can return boolean values 
 
def function_x():
    return True

print(function_x())

if function_x():
    print("function_x() is True")
else:
    print("function_x() is False")


# using isinstance() to check the type of a variable

x = 10

x = "very strong"
print(isinstance(x, int)) # True
