# the wrong example

myAge =  25
# info = " my age is " + myAge + " years old"

# print(info)

# the right example using format  f"string

information = f"my age is {myAge} years old"

print(information) # this will print the string with the value of myAge


# placeholder can include a modifier, such as a number of decimal places

pi = 3.14159
pi_info = f"the value of pi is {pi:.2f}"

print(pi_info) # this will print the string with the value of pi with 2 decimal places

r = 5
luas_lingkaran = pi * r**2
print(f"luas lingkaran dengan jari-jari {r} adalah {luas_lingkaran}" )
