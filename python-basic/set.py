# sets are used to store multiple items in a single variable
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Sets are written with curly brackets.
# A set cannot have two items with the same value.

# Create a Set
thisset = {"apple", "banana", "cherry"}
print(thisset) # {'banana', 'cherry', 'apple'}
# Set items are unordered, so you cannot be sure in which order the items will appear.

# all from the set is simmilar to list

# set constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) # {'banana', 'cherry', 'apple'}

# isinya bisa di tambah dan di hapus, tidak bisa di ubah

# access set items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x) # apple banana cherry

# check if item exist
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset) # True

# we cannot access set items by index or range 
# but we can use loops to access the items


# add sets item using update()
thisset = {"apple", "banana", "cherry"}
set02 = {"orange", "mango", "grape"}
thisset.update(set02)
print(thisset) # {'banana', 'cherry', 'apple', 'orange', 'mango', 'grape'}


# add sets it can be any iterable object like list, tuple, dictionary
thisset = {"apple", "banana", "cherry"}
secondset = ("orange", "mango", "grape")
thisset.update(secondset)
print(thisset) # {'banana', 'cherry', 'apple', 'orange', 'mango', 'grape'}


# remove item from set
# using remove() method, and discard() method
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
thisset.discard("cherry")

secondset = {"ayam", "kambing", "sapi"}
secondset.pop()
print(secondset) # {'kambing', 'sapi'}

# pop() method removes a random item from the set, because sets are unordered

# using clear() method
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) # set()

# delete the set completely
thisset = {"apple", "banana", "cherry"}
del thisset 
# print(thisset) # NameError: name 'thisset' is not defined

# join sets
# using union() method and update() method
set01 = {"apple", "banana", "cherry"}
set02 = {"orange", "mango", "grape"}
set03 = set01.union(set02)
print(set03) # {'banana', 'cherry', 'apple', 'orange', 'mango', 'grape'}

set01.union(set02) # {'banana', 'cherry', 'apple', 'orange', 'mango', 'grape'}
print(set01) # {'banana', 'cherry', 'apple'}

# using update() method
set01 = {"apple", "banana", "cherry"}
set02 = {"orange", "mango", "grape"}
set01.update(set02)

set03 = set01.update(set02) # {'banana', 'cherry', 'apple', 'orange', 'mango', 'grape'}
print(set03) # None
# update tidak mengembalikan nilai, tetapi mengubah set01

# using | operator , but this will not change the original set
set01 = {"apple", "banana", "cherry"}
set02 = {"orange", "mango", "grape"}
set03 = set01 | set02

# join multiple sets using union() method
set01 = {"apple", "banana", "cherry"}
set02 = {"orange", "mango", "grape"}
set03 = {"kiwi", "melon", "mango"}
set04 = set01.union(set02, set03)

# | operator only works with the sets with the same type , sets with sets


# intersection of sets
set01 = {"apple", "banana", "cherry"}
set02 = {"orange", "banana", "grape"}
set03 = set01.intersection(set02)
print(set03) # {'banana'}

# intersection akan mengembalikan set baru yang berisi item yang ada di kedua set
# using & operator
set01 = {"apple", "banana", "cherry"}
set02 = {"orange", "banana", "grape"}
set03 = set01 & set02
print(set03) # {'banana'}

# difference of sets
set01 = {"apple", "banana", "cherry"}
set02 = {"orange", "banana", "grape"}
set03 = set01.difference(set02)
print(set03) # {'apple', 'cherry'}

# difference akan mengembalikan set baru yang berisi item yang ada di set01 tetapi tidak ada di set02
# difference ini sama dengan set01 - set02

# using - operator
set01 = {"apple", "banana", "cherry"}
set02 = {"orange", "banana", "grape"}
set03 = set01 - set02
print(set03) # {'apple', 'cherry'}

# intersection_update() method and difference_update() method
# tidak mengembalikan nilai, tetapi mengubah set01 
# tidak dapat menyimpan hasilnya ke dalam variabel lain

# symmetric_difference() method
set01 = {"apple", "banana", "cherry"}
set02 = {"orange", "banana", "grape"}
set03 = set01.symmetric_difference(set02)
print(set03) # {'apple', 'cherry', 'orange', 'grape'}

# symmetric_difference() method mengembalikan set baru yang berisi item yang ada di set01 dan set02 tetapi tidak ada di kedua set
# using ^ operator
set01 = {"apple", "banana", "cherry"}
set02 = {"orange", "banana", "grape"}
set03 = set01 ^ set02
print(set03) # {'apple', 'cherry', 'orange', 'grape'}

# A = {1, 2, 3}
# B = {3, 4, 5}

# intersection         → {3}
# difference (A - B)   → {1, 2}
# symmetric_difference → {1, 2, 4, 5}
