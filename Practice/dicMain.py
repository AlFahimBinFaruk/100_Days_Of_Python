# dictionary is a key value pair data storage,
# the key can be both string or integer
# dictionary is mutable

myDict={
    "name":"fahim",
    "age":33,
    "married":False,
    "address":{
        "city":"ctg",
        "country":"BD"
    },
    1:"fahim",
    "name":"Zayn"
}
print(myDict)
# print(myDict["name"])
# print(myDict["address"]["city"])
# print(myDict[1])

# this will throw error as name3 is not there
# print(myDict["name3"])

# but this will give None will not throw an error
# print(myDict.get("name3"))

# it will create a new key name salary as it is not already there then the value will be 333,just like append
# myDict["salary"]=333

# it will update the value of name
# myDict["name"]="Al fahim bin faruk"
# print(myDict)

# print(myDict.keys())
# print(myDict.values())

# it will turn the dictionary into an array of tuples
# myTub=myDict.items()
# print(myTub)

updateDict = {"work": "Backend dev", "status": "unemployed"}
myDict.update(updateDict)
print(myDict)