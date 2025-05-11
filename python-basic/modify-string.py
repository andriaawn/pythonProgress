# using upper() method\

greatings = "hello, welcome to the python"
print(greatings.upper()) # convert to upper case

print(greatings.lower()) # convert to lower case


# remove whitespace from the beginning and end of a string
simpleGreatings = " selamat datang , senang bertemu denganmu "
print(simpleGreatings.strip())

print(simpleGreatings.strip().replace("selamat datang", "welcome"))

# using split()

print(simpleGreatings.strip().split(","))

