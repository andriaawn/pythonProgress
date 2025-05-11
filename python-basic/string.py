print("it's a string")

print('it"s not a string')

# "hello" and 'hello' are the same


# assign values string to variable  

greating = "hello"
print(greating)

# multiline string
greating = """hello im andriawan, i live 
in jakarta, i am a software engineer"""
print(greating)

# string as array 

greating = "hello, im andriawan"
print(greating[0]) # h
print(greating[1]) # e
print(greating[2]) # l

# array identik dengan [] sebagai index dari string, dimulai dari 0


# looping array on string

colors = "red, blue, yellow"
colors = "only red"
for x in colors:
    print(x) # r e d ,   b l u e ,   y e l l o w


# string lenght

color = "yellow"

print(len(color)) # 6
print(len(colors)) # 8

# check string

txt = "hello, welcome to my world"
print("welcome" in txt) # True
print("the words" in txt) # False


# using if statement
txt = "hello, welcome to my world"

if "welcome" in txt:
    print("yes, 'welcome' is present.")
else:
    print("there is no 'welcome' in the text")

txt = "im doing great, thank you"
if "great" not in txt:
    print("yes, 'great' is not present.")
else:
    print("there is 'great' in the text")


