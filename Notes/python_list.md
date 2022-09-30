### python list
* basic syntax
```bash
mylist = ["apple", "banana", "cherry"] 
```

* Access list item
```bash
thislist = ["apple", "banana", "cherry"]

# print the 1th index of the list
print(thislist[1]) 

# print the last item of the list
print(thislist[-1])
```

* Slice list
```bash
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) 
```

* Change item
```bash
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) 
```

* add item
```bash
01.Using append()
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) 

02.Using insert()
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
```

* Extend list
```bash
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) 
```

* Remove item
```bash
# 01.remove()
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) 

# 02.pop()
thislist = ["apple", "banana", "cherry"]

# removes the item at 1th index
thislist.pop(1)

# removes the last item
thislist.pop()
print(thislist)

# 03.del keyword
thislist = ["apple", "banana", "cherry"]
# delete the item at 0th index
del thislist[0]

# delete the whole list
del thislist
print(thislist)

# clear()
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
```

* Loop in list
```bash
# 01.For loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) 
  
# 02. While loop
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# 03. List Comprehension
[print(x) for x in thislist]
```

* List comprehension
```bash
# Syntax
newlist = [expression for item in iterable if condition == True] 

# Ex 01
newlist = [x for x in fruits]

# Ex 02
newlist = [x for x in fruits if x != "apple"]

# Ex 03
newlist = [x for x in range(10) if x < 5]

# Ex 04
newlist = [x.upper() for x in fruits]

# Ex 05
newlist = [x if x != "banana" else "orange" for x in fruits]
```

* Sort list
```bash
# Ex 01
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Ex 02 : while reverse in True
thislist.sort(reverse = True)
print(thislist) 

# Ex 03 : case -insensitive sorting
thislist.sort(key = str.lower)
print(thislist)

# Ex 04 Reverse the order
thislist.reverse()
print(thislist)
```

* Custom Sort list
```bash
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist) 
```

* Copy list
```bash
thislist = ["apple", "banana", "cherry"]

# Ex 01 with copy()
mylist = thislist.copy()
print(mylist) 

# Ex 02 with list()
mylist = list(thislist)
print(mylist)
```

* Join two or more list
```bash
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

# Ex 01 : with + operator
list3 = list1 + list2
print(list3) 

# Ex 02 : with for loop
for x in list2:
  list1.append(x)

print(list1)


# Ex 03 : with extend()
list1.extend(list2)
print(list1)
```

### List methods
* [Python List methods - very important]("https://www.w3schools.com/python/python_lists_methods.asp")

### Important resources
* [Python list - very important]("https://www.w3schools.com/python/python_lists.asp")
