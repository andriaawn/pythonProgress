# dictionary are used to store data values in key:value pairs
# A dictionary is a collection which is unordered, changeable and does not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

print(thisdict["brand"]) # Ford
print(thisdict.get("model")) # Mustang

# duplicate not allowed
# will overwrite the existing value
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

print(len(thisdict)) # 3

# dictionary with mixed data types
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "is_electric": False
}
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'is_electric': False}

# dictionary constructor
thisdict = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# Accessing items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = thisdict["model"]
print(x) # Mustang

# Accessing items using get()
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict.get("model")

# get key of dictionary
x = thisdict.keys() # dict_keys(['brand', 'model', 'year'])

# get value of dictionary
x = thisdict.values() # dict_values(['Ford', 'Mustang', 1964])

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

car["color"] = "red"

print(car) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

# get items dictionary as list of tuples
x = thisdict.items() # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change


# check if key exists
modelCar = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964    
}

if "brand" in modelCar:
    print("Yes, 'brand' is one of the keys in the modelCar dictionary") # Yes, 'brand' is one of the keys in the modelCar dictionary

# change value of key

theBooks = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925
}
theBooks["year"] = 1926


# using update() method
theBooks.update({"year": 1926})

# adding items
# is done using the new index key and assigning a value to it
theBooks["publisher"] = "Scribner"
print(theBooks) # {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1926, 'publisher': 'Scribner'}
# menambahkan item baru yang tidak ada di dalam dictionary sebelumnya, dan key tidak boleh sama

# update() method are also used to add new items if the key does not exist


## removing items 
# use pop() method
theBooks = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925
}
theBooks.pop("year")
print(theBooks) # {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'}

# use popitem() method, removes the last inserted item
theBooks.popitem()
print(theBooks) # {'title': 'The Great Gatsby'}

# del keyword
theBooks = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925
}
del theBooks["year"]
print(theBooks) # {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'}

# del can also delete the dictionary completely
theBooks = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925
}
del theBooks

# clear() method
theBooks = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925
}

theBooks.clear()
print(theBooks) # {}

# loop dictionary

animalDict = {
    "animal": "dino",
    "color": "black"
}

for x in animalDict:
    print(x)
    # this print all key of dictionary

# it can use value()
for x in animalDict.values():
    print(x)

# it can use keys()
for x in animalDict.keys():
    print(x)

for x in animalDict:
    print(animalDict[x])
    # print all value of dictionary


# access key, value through items()
for x, y in animalDict.items():
    print(x, y)


# copy dictionary 
animals = animalDict.copy()
print(animals)

# using dict
animals = dict(animalDict)


# nested dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

child1 = {
    "name": "awan",
    "birthday": "april"
}
child2 = {
    "name": "indra",
    "birthday": "june"
}

newfamily = {
    "child1": child1,
    "child2": child2
}

## access items
print(newfamily["child2"]["name"])

# loop nested dictionary
for x, obj in newfamily.items():
    print(x)

    for y, in obj:
        print(y + ":", obj[y])