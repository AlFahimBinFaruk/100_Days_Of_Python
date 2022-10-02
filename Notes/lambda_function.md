### Python Lambda
* A lambda function is a small anonymous function.
* A lambda function can take any number of arguments, but can only have one expression.
* Syntax :
```bash
# Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5)) 
```
* Lambda functions can take any number of arguments:
```bash
# Ex 01
x = lambda a, b : a * b
print(x(5, 6))

# Ex 02
y = lambda a, b, c : a + b + c
print(y(5, 6, 2)) 

```

### Why Use Lambda Functions?
* The power of lambda is better shown when you use them as an anonymous function inside another function.
* Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
```bash
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) 
print(mytripler(11))
```

### Important resources
* [Python lambda](https://www.w3schools.com/python/python_lambda.asp)