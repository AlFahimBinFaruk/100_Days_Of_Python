### Functions
* A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
* In Python a function is defined using the def keyword:
```bash
def my_function():
  print("Hello from a function")

my_function()
```

### Arguments
* Information can be passed into functions as arguments.
* Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
* The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:
```bash
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus") 
```

### Parameters or Arguments?
* The terms parameter and argument can be used for the same thing: information that are passed into a function.
* From a function's perspective:
  * A **parameter** is the variable listed inside the parentheses in the function definition.
  * An **argument** is the value that is sent to the function when it is called.

### Number of Arguments
* By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

### Arbitrary Arguments, *args
* If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
* This way the function will receive a tuple of arguments, and can access the items accordingly:
```bash
def my_function(*kids):
  print("The youngest child is " + kids[2])

# it will throw error if you don't pass any args
my_function("Emil", "Tobias", "Linus") 
```

### Keyword Arguments
* You can also send arguments with the key = value syntax.
* This way the order of the arguments does not matter.
```bash
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

# Normal arguments
my_function("Emil", "Tobias","Linus") 

# Keyword arguments
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") 
```

### Arbitrary Keyword Arguments, **kwargs
* If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
* This way the function will receive a dictionary of arguments, and can access the items accordingly:
```bash
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes") 
```

### Default Parameter Value
* The following example shows how to use a default parameter value.
* If we call the function without argument, it uses the default value:
```bash
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil") 
```

### return value
```bash
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
```

### The pass Statement
* function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
```bash
def myfunction():
  pass 
```