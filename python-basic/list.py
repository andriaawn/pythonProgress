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
