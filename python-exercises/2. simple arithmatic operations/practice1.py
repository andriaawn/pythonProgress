"""
Asks the user for two numbers.
Converts the inputs into floats.
Performs addition, subtraction, multiplication, and division.
Prints the results with clear messages.
"""

# Ask the user for two numbers
number1 = input("Enter the first your number: ")
number2 = input("Enter the second your number: ")

# Convert the inputs into floats
number1 = float(number1)
number2 = float(number2)

# Perform addition, subtraction, multiplication, and division
number3 = number1 + number2
number4 = number1 - number2
number5 = number1 * number2
number6 = number1 / number2

# Print the results with clear messages
print(f"The sum of {number1} and {number2} is {number3}")
print(f"The difference of {number1} and {number2} is {number4}")
print(f"The product of {number1} and {number2} is {number5}")
print(f"The quotient of {number1} and {number2} is {number6}")


