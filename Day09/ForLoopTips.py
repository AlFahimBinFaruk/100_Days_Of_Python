symbols = '$¢£¥€¤'

# Example 01
codeOne = []
for symbol in symbols:
    codeOne.append(ord(symbol))
print(codeOne)

# Example 02 : this is called List comprehensions
codeTwo=[ord(symbol) for symbol in symbols]
print(codeTwo)