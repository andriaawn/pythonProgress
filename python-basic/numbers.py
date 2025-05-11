# Int is a whole number (positive or negative) without decimals of unlimited length
x = 5
print(x)
print(type(x))

# Float is a number with a decimal point
y = 5.0
print(y)
print(type(y))

y1 = 10e3 # 10 * 10^3
print(y1)   # 10000.0
print(type(y1)) # <class 'float'>


# Complex numbers are written with a "j" as the imaginary part
z = 5j
print(z)
print(type(z))

# what is imaginary part? 
# In mathematics, the imaginary unit or unit imaginary number is a solution to the quadratic equation x^2 + 1 = 0.

# Type Conversion
# You can convert from one type to another with the int(), float(), and complex() methods:

# Convert from int to float:
a = 9
a = float(x)
print(a)    # 9.0
print(type(a)) # <class 'float'>

b = 7.9
b = int(b)
print(b)    # 7 
print(type(b)) # <class 'int'>

c = 5
c = complex(c)
print(c)    # (5+0j)
print(type(c)) # <class 'complex'>

# Random Number
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
import random

print(random.randrange(1, 10)) # 1 to 9

# Random number between 0 and 1
print(random.random()) # 0.0 to 1.0

# Random number between 0 and 100
print(random.random() * 100) # 0.0 to 100.0

# Random number between 1 and 100
print(random.random() * 100 + 1) # 1.0 to 101.0 

# Random number between 1 and 100
print(random.randint(1, 100)) # 1 to 100 

# Random number between 1 and 100
print(random.uniform(1, 100)) # 1.0 to 100.0 



