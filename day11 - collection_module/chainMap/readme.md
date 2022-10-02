### Chainmap
* A ChainMap encapsulates many dictionaries into a single unit and returns a list of dictionaries.
* syntax:
```bash
# Python program to demonstrate
# ChainMap


from collections import ChainMap

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
d4 = {'g':44,'h':33}

# Defining the chainmap
c = ChainMap(d1, d2, d3)

# using new_child() to add new dictionary
c.new_child(d4)

# Accessing Values using key name
print(c['a'])

# Accessing values using values()
# method
print(c.values())

# Accessing keys using keys()
# method
print(c.keys())

print(c)
```
