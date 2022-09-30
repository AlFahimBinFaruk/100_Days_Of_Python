### Dictionaries
* Dictionaries are used to store data values in key:value pairs.
* A dictionary is a collection which is **ordered***, **changeable** and **do not allow duplicates**.
* syntax:
```bash
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict) 
```
* Nested dictionary:
```bash
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
```

### Access item
```bash
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Ex 01
x = thisdict["model"]

# Ex 02
x = thisdict.get("model")
```
* Get Keys
  * The keys() method will return a list of all the keys in the dictionary.
```bash
x = thisdict.keys() 
```

* Get Values
  * The values() method will return a list of all the values in the dictionary.
```bash
x = thisdict.values() 
```

* Get Items
  * The items() method will return each item in a dictionary, as tuples in a list.
```bash
x = thisdict.items() 
```

* Check if Key Exists
  * To determine if a specified key is present in a dictionary use the in keyword:
```bash
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary") 
```

### Change/update existing item
```bash
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Ex 01
thisdict["year"] = 2018

# Ex 02
thisdict.update({"yearTwo": 2020})

```

### Add Item
```bash
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Ex 01
thisdict["color"] = "red"

# Ex 02
thisdict.update({"colorTwo": "red"})
```

### Remove item
* pop() : The pop() method removes the item with the specified key name:
```bash
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.pop("model")
print(thisdict) 
```

* popitem() : The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
```bash
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict) 
```

* del keyword:
```bash
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Ex 01 : del removes the item with the specified key name:
del thisdict["model"]

# Ex 02 : del keyword can also delete the dictionary completely:
del thisdict
```

* The clear() method empties the dictionary:
```bash
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict) 
```

### Loop in a dictionary
* You can loop through a dictionary by using a for loop.
* When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
* Print all key names in the dictionary, one by one:
```bash
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
```

* Print all values in the dictionary, one by one:
```bash
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x]) 
```

* You can also use the values() method to return values of a dictionary:
```bash
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)
```

* You can use the keys() method to return the keys of a dictionary:
```bash
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x) 
```
* Loop through both keys and values, by using the items() method:
```bash
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y) 
```

### copy dictionary
* Make a copy of a dictionary with the copy() method:
```bash
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict) 
```

* Another way to make a copy is to use the built-in function dict().
```bash
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict) 
```

### Dictionaries methods
* [Dictionaries all methods](https://www.w3schools.com/python/python_dictionaries_methods.asp)

### Important resources
* [Python dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)