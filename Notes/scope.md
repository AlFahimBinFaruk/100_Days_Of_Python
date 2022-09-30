### Python Scope
* A variable is only available from inside the region it is created. This is called scope.

#### Local Scope
* A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
```bash
def myfunc():
  x = 300
  print(x)

myfunc() 
```

#### Global Scope
* A variable created in the main body of the Python code is a global variable and belongs to the global scope.
* Global variables are available from within any scope, global and local.
```bash
x = 300

def myfunc():
  print(x)

myfunc()

print(x) 
```
* Naming Variables
  * If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):
```bash
x = 300

# The function will print the local x, and then the code will print the global x:
def myfunc():
  x = 200
  print(x)

myfunc()

print(x) 
```

### Global Keyword
* If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
* The global keyword makes the variable global.
```bash
def myfunc():
  global x
  x = 300

myfunc()

print(x) 
```

### Important resources
* [Python scopes](https://www.w3schools.com/python/python_scope.asp)