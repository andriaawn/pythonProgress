# tuples is a collection of ordered and unchangeable elements
# tuples are written with round brackets
# tuples can contain different data types
# tuples can be empty
# tuples are used to store multiple items in a single variable


mytuples = ("apple", "banana", "cherry")

# tuple is mutable / tidak bisa diubah
mytuples = ("apple", "banana", "cherry")
mytuples[0] = "orange"  # this will raise an error
print(mytuples) # Output: TypeError: 'tuple' object does not support item assignment

# tuples are used for key in dictionaries
mydict = {
    ("apple", "banana"): "fruit",
    ("carrot", "broccoli"): "vegetable"
}
print(mydict[("apple", "banana")])  # Output: fruit

# tuples allow duplicate values
mytuple = ("apple", "banana", "cherry", "apple")
print(mytuple)  # Output: ('apple', 'banana', 'cherry', 'apple')

# tuple length
# using leng() function
mytuple = ("apple", "banana", "cherry")
print(len(mytuple))  # Output: 3

# if you only have one item in a tuple, you must add a comma after the item
mytuple = ("apple",)

# tuple contains different data types
mytuple = ("apple", 1, 2.5, True)

# to check data type of a tuple
# using type() function
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))  # Output: <class 'tuple'>

# tuple constructors
# using tuple() constructor
mytuple = tuple(("apple", "banana", "cherry"))
print(mytuple)  # Output: ('apple', 'banana', 'cherry')

# tuple access is similar to list access

# update tuple
# tuples are immutable, so you cannot change the value of a tuple
# but you can convert it to a list, change the value, and convert it back to a tuple

mytuple = ("apple", "banana", "cherry")
mytupleIntoList = list(mytuple)
mytupleIntoList[0] = "orange"
mytuple = tuple(mytupleIntoList)
print(mytuple)  # Output: ('orange', 'banana', 'cherry')

# diubah menjadi list dan diubah menjadi tuple lagi

# add items
# convert tuple to list
# using operator +
mytuple = ("apple", "banana", "cherry")
y = ("kiwi",)
mytuple += y
print(mytuple)  # Output: ('apple', 'banana', 'cherry', 'kiwi')

# remove items
# convert tuple to list
# using the del keyword
mytuple = ("apple", "banana", "cherry")
del mytuple
print(mytuple)  # Output: NameError: name 'mytuple' is not defined

# unpacking tuples
# unpacking is the process of assigning the values of a tuple to variables

mytuples = ("apple", "banana", "cherry")
a, b, c = mytuples
print(a)  # Output: apple
print(b)  # Output: banana
print(c)  # Output: cherry

# using the asterisk (*) operator
mytuples = ("apple", "banana", "cherry", "kiwi", "orange")
a, b, *c = mytuples
print(a)  # Output: apple
print(b)  # Output: banana
print(c)  # Output: ['cherry', 'kiwi', 'orange'] is a list

# add asterisk (*) to the middle of the variable name
mytuples = ("apple", "banana", "cherry", "kiwi", "orange")
a, *b, c = mytuples
print(a)  # Output: apple
print(b)  # Output: ['banana', 'cherry', 'kiwi']
print(c)  # Output: orange

# loop tuples is similar to loop lists
mytuples = ("apple", "banana", "cherry")
for x in mytuples:
    print(x)  # Output: apple banana cherry
# using the range() and len() functions
mytuples = ("apple", "banana", "cherry")
for i in range(len(mytuples)):
    print(mytuples[i])  # Output: apple banana cherry
# using the while loop
mytuples = ("apple", "banana", "cherry")
i = 0
while i < len(mytuples):
    print(mytuples[i])  # Output: apple banana cherry
    i += 1

# join tuples
# it can be done by using the + operator
mytuple1 = ("apple", "banana", "cherry")
mytuple2 = ("kiwi", "orange")
mytuple3 = mytuple1 + mytuple2

# it can be multiplied by using the * operator
mytuple1 = ("apple", "banana", "cherry")
mytuple2 = mytuple1 * 2
print(mytuple2)  # Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')


# tuple methods
# count() method
# returns the number of times a specified value occurs in a tuple
mytuple = ("apple", "banana", "cherry", "apple")
print(mytuple.count("apple"))  # Output: 2
# index() method
# searches the tuple for a specified value and returns the position of where it was found
mytuple = ("apple", "banana", "cherry")
print(mytuple.index("banana"))  # Output: 1


