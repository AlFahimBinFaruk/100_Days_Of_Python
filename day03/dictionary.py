'''
Dictionaries are used to store data values in key:value pairs. 
A dictionary is a collection which is ordered, 
changeable and do not allow duplicates.
'''
'''
if any key is repeated then the last value of that key will be valid
'''
# syntax
myDict = {
    "name": "Al fahim",
    "age": 33,
    "married": False,
    "skill": ["javascript", "python"],
    "anotherDict": {
        'address': 'CTG',
        'country': 'BD'
    },
    1: 2,
    1: 5
}

# access a value by key name
print(myDict["age"], myDict["name"])
print(myDict["skill"])
print(myDict["anotherDict"]["country"])

# access value using get
'''both myDict["anotherDict"] and myDict.get("anotherDict") are same but  get() wont give error if it dont find anything'''
print(myDict.get("anotherDict"))
print(myDict.get("anotherDic4t"))
print(myDict["anotherDicfft"])

# dictionary is mutable
myDict["age"] = 45
print(myDict["age"])

''' Dictionary methods'''
# get only keys of a dictionary
print(myDict.keys())

# print key by convertion them to a list
print(list(myDict.keys()))

# get only values of dictionary
print(list(myDict.values()))

# items() turn dictionary into a tuple kind of type (retruns both key and value)
print(list(myDict.items()))

# update dictionary
updateDict = {"work": "Backend dev", "status": "unemployed"}
myDict.update(updateDict)
print(myDict)
