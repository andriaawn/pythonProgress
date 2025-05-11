# casting is used to specify the data type of an object
# There are several built-in functions to perform casting
# int() - constructs an integer number from an integer literal, a float literal (by rounding down to the previous whole number), or a string literal (providing the string represents a whole number)
# float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
# str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

# in indonesia casting is called "konversi tipe data"

# Example 
# Integers:
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

# Floats:
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
W = float("1.9") # w will be 1.9

# Strings:
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

# Example
# Convert from one type to another:
a = 1    # int
b = 2.8  # float
c = 1j   #
# convert from int to float:

a = float(a) # a will be 1.0
b = int(b) # b will be 2
c = int(c) # c will be error because complex number can't be converted to int

print(a, b, c) # print the result
# Output: 1.0 2 1j





