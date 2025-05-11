# lists are used to store multiple items in a single variable
# list is a collection which is ordered and changeable. allows duplicate members

thisLists = ["apple", "banana", "cherry"]

print(thisLists)  # ['apple', 'banana', 'cherry']
print(type(thisLists))  # <class 'list'>

print(len(thisLists))  # 3

# list indexing
print(thisLists[0])  # apple
print(thisLists[1])  # banana
print(thisLists[2])  # cherry

# if you add a new item to the list, it will be added to the end of the list

thisLists.append("orange")
print(thisLists)  # ['apple', 'banana', 'cherry', 'orange']

# list can contain different data types
thisLists = ["apple", 1, True, 3.14]

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# positive indexing start from 0
print(thisLists[0])  # apple

# negative indexing start from -1
print(thisLists[-1])  # 3.14
print(thisLists[-2])  # True

# range of indexes
updateList = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(updateList[2:5])  # ['cherry', 'orange', 'kiwi']
print(updateList[:4])  # ['apple', 'banana', 'cherry', 'orange']
print(updateList[2:])  # ['cherry', 'orange', 'kiwi', 'mango']
print(updateList[-4:-1])  # ['orange', 'kiwi', 'mango']
print(updateList[-4:])  # ['orange', 'kiwi', 'mango']

# check if item exists in list
print("apple" in updateList)  # True

if "apple" in updateList:
    print("Yes, 'apple' is in the fruits list")  # Yes, 'apple' is in the fruits list

# if "apple" not in updateList:
#     print("No, 'apple' is not in the fruits list")  # No, 'apple' is not in the fruits list


# change list item
changeList = ["apple", "banana", "cherry"]
print(changeList)  # ['apple', 'banana', 'cherry']
changeList[1] = "blackcurrant"
print(changeList)  # ['apple', 'blackcurrant', 'cherry']
changeList[1:2] = ["watermelon", "kiwi"]
print(changeList)  # ['apple', 'watermelon', 'kiwi', 'cherry']

# insert items
# using insert() method
insertList = ['apple', 'banana', 'cherry']
print(insertList)  # ['apple', 'banana', 'cherry']
print(insertList[1])  # banana
insertList.insert(1, "orange") # [''apple', 'orange', 'banana', 'cherry']

# append items 
# using append() method
# append() method adds an item to the end of the list
appentList = ['apple', 'banana', 'watermelon']
appentList.append('kiwi')
print(appentList)  # ['apple', 'banana', 'watermelon', 'kiwi']
appentList.append("orange")
print(appentList)  # ['apple', 'banana', 'watermelon', 'kiwi', 'orange']


# extend() method
# using extend() method to add multiple items to the list
# extend() method adds the elements of a list (or any iterable), to the end of the current list
# Note: If you want to add a list to another list, use the append() method instead.
list1 = ['apple', 'banana', 'cherry']
list2 = ['kiwi', 'orange']
list1.extend(list2)
print(list1)  # ['apple', 'banana', 'cherry', 'kiwi', 'orange']


# remove items
# using remove() method
# remove() method removes the first item with the specified value
removeList = ['apple', 'banana', 'cherry']
removeList.remove("banana")
print(removeList)  # ['apple', 'cherry']

# if there are multiple items with the same value, only the first one will be removed
removeList.append("apple")
print(removeList)  # ['apple', 'cherry', 'apple']
removeList.remove("apple")
print(removeList)  # ['cherry', 'apple']

# remove specified index using pop() method
# pop() method removes the specified index, (or the last item if index is not specified)
popList = ['apple', 'banana', 'cherry']
popList.pop(1)
print(popList)  # ['apple', 'cherry']
popList.pop()
print(popList)  # ['apple']

# del keyword
# The del keyword removes the specified index
# The del keyword can also delete the list completely

del popList[0]
print(popList)  # []

delList = ['apple', 'banana', 'cherry']
del delList
print(delList)  # NameError: name 'delList' is not defined

# clear() method
# The clear() method empties the list
# The list still exists, but it is empty
clearList = ['apple', 'banana', 'cherry']
clearList.clear()
print(clearList)  # []

# loop through a list
loopList = ['apple', 'banana', 'cherry']
for x in loopList:
    print(x)  # apple banana cherry

# loop through the index numbers
for i in range(len(loopList)):
    print(loopList[i])  # apple banana cherry

# while loop 
# using while loop to loop through a list
whileLoopsList = ['apple', 'banana', 'cherry']
i = 0 

while i < len(whileLoopsList):
    print(whileLoopsList[i])
    i += 1  # apple banana cherry

# looping using list comprehension
# list comprehension is a concise way to create lists
# it consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses
# the result will be a new list resulting from evaluating the expression in the context of the for and if clauses
# list comprehension is more compact and faster than the traditional for loop
# syntax: newlist = [expression for item in iterable if condition == True]
# example: create a new list with the values of the original list, but only if the value is even
# original list
originalList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new list
newList = [x for x in originalList if x % 2 == 0]

print(newList)  # [2, 4, 6, 8, 10]


thisItems = ["apple", "mango", "cherry"]
[print(x) for x in thisItems]
# apple mango cherry


# list comprehension
allfruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newFruits = []

for x in allfruits:
    if "a" in x:
        newFruits.append(x)

print(newFruits) # ['apple', 'banana', 'mango']

# with list comprehension, you can do this in one line
newFruits = [x for x in allfruits if "a" in x]

print(newFruits) # ['apple', 'banana', 'mango']

# the sintax 
# newFruits = [expression for item in iterable if condition == True]
# the conndition is like a filter that only accepts the items that evaluate to True

# the condition is optional
# if you do not want to filter the items, you can use an empty condition
newFruits = [x for x in allfruits]

# you can use range() to create an iterable
newFruits = [x in newFruits for x in range(6)]
print(newFruits) # [0, 1, 2, 3, 4, 5]
newFruits = [x in newFruits for x in range(10) if x > 5]
print(newFruits) # [6, 7, 8, 9]

# set value using expression
# you can set the values of a list using an expression
newFruits = [x.upper() for x in allfruits]
print(newFruits) # ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

# set value using expression and condition
newFruits = ['hello' for x in allfruits]

theFruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
theFruits = [x if x != 'banana' else 'orange' for x in theFruits]
print(theFruits)  # ['apple', 'orange', 'cherry', 'kiwi', 'mango']



# sort list 
# sort() method
# sort() method sorts the list ascending by default, and you can also make a function to decide the sorting criteria(s)
# akan mengurutkan list secara ascending yaitu dari yang terkecil ke yang terbesar

sortList = ['banana', 'cherry', 'apple']
sortList.sort()
print(sortList)  # ['apple', 'banana', 'cherry']
sortList.sort(reverse=True)
print(sortList)  # ['cherry', 'banana', 'apple']

theNumericList = [100, 50, 65, 82, 23]
theNumericList.sort()
print(theNumericList)  # [23, 50, 65, 82, 100]

# if you want to sort descending, use the reverse parameter
theNumericList.sort(reverse=True)

print(theNumericList)  # [100, 82, 65, 50, 23]

# customize sort function
# you can customize the sort order by using a function
def myFunc(e):
    return abs(e - 50)

theNumericList = [100, 50, 65, 82, 23]
theNumericList.sort(key=myFunc)
print(theNumericList)  # [50, 65, 82, 23, 100]

# case insensitive sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters

Fruits = ['banana', 'Orange', 'Kiwi', 'cherry']
Fruits.sort()
print(Fruits)  # ['Kiwi', 'Orange', 'banana', 'cherry']

# we can using .lower() method to perform a case-insensitive sort
Fruits = ['banana', 'Orange', 'Kiwi', 'cherry']
Fruits.sort(key=str.lower)
print(Fruits)  # ['banana', 'cherry', 'Kiwi', 'Orange']

# using reversed() method
# reversed() method returns a reversed iterator object
# reversed() method membalikkan urutan list dari yang terakhir ke yang pertama

reversedList = ['banana', 'cherry', 'apple']
reversedList.reverse()
print(reversedList)  # ['apple', 'cherry', 'banana']


## copy list
# copy() method
# list() method
# slice operator

copyList = ['apple', 'banana', 'cherry']
myCopyList = copyList.copy()

myCopyList = list(copyList)
myCopyList = copyList[:]

## join two lists
# using + operator
list1 = ['apple', 'banana', 'cherry']
list2 = ['guava', 'kiwi']

list3 = list1 + list2
print(list3)  # ['apple', 'banana', 'cherry', 'guava', 'kiwi']

for x in list2:
    list1.append(x)
print(list1)  # ['apple', 'banana', 'cherry', 'guava', 'kiwi']

list1.extend(list2)
print(list1)  # ['apple', 'banana', 'cherry', 'guava', 'kiwi', 'guava', 'kiwi']



