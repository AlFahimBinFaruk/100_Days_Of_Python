### What is a Module?
* Consider a module to be the same as a code library.
* A file containing a set of functions you want to include in your application.

### Creating a module
* see above example to know everything.

### Re-naming a Module
* You can create an alias when you import a module, by using the as keyword: see **test.py**

### Built-in Modules
* There are several built-in modules in Python, which you can import whenever you like.
```bash
import platform

x = platform.system()
print(x) 
```

### Using the dir() Function
* There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
```bash
import platform

x = dir(platform)
print(x) 
```

### Import From Module
* You can choose to import only parts from a module, by using the from keyword : see **test.py**

### Important resources
* [Python Modules](https://www.w3schools.com/python/python_modules.asp)