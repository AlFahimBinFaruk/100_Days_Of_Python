### Python JSON
* JSON is a syntax for storing and exchanging data.
* JSON is text, written with JavaScript object notation.

### JSON in Python
* Python has a built-in package called json, which can be used to work with JSON data.

### Convert from JSON to Python:
```bash
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"]) 
```

### Convert from Python to JSON
```bash
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
```

* You can convert Python objects of the following types, into JSON strings:
  * dict
  * list
  * tuple
  * string
  * int
  * float
  * True
  * False
  * None
```bash
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None)) 
```

#### When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

| Python | JSON   |
|--------|--------|
| dict   | Object |
| list   | Array  |
| tuple  | Array  |
| str    | String |
| int    | Number |
| float  | Number |
| True   | true   |
| False  | false  |
| None   | null   |


### Format the Result
* The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
* The json.dumps() method has parameters to make it easier to read the result:
```bash
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4)) 
```

* You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:
```bash
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(".", "="))) 

# this is the default separators value
# print(json.dumps(x, indent=4, separators=(",", ":"))) 
```

### Order the Result
* The json.dumps() method has parameters to order the keys in the result:'
```bash
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True)) 
```

### Important resources
* [Python JSON](https://www.w3schools.com/python/python_json.asp)