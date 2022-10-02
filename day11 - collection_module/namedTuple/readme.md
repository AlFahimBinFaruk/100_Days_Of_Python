### NamedTuple
* A NamedTuple returns a tuple object with names for each position which the ordinary tuples lack. For example, consider a tuple names student where the first element represents fname, second represents lname and the third element represents the DOB. Suppose for calling fname instead of remembering the index position you can actually call the element by using the fname argument, then it will be really easy for accessing tuples element. This functionality is provided by the NamedTuple.

### Conversion Operations 
*  _make(): This function is used to return a namedtuple() from the iterable passed as argument.
* _asdict(): This function returns the OrdereDict() as constructed from the mapped values of namedtuple().
```bash
# Python code to demonstrate namedtuple()

from collections import namedtuple

# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# Access using index
print("The Student age using index is : ", end="")
print(S[1])

# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)

# initializing iterable
li = ['Manjeet', '19', '411997']


# using _make() to return namedtuple() - make li a namedTuple
print("The namedtuple instance using iterable is  : ")
print(Student._make(li))


# using _asdict() to return an OrderedDict() - return S namedTuple as a normal dictionary
print("The OrderedDict instance using namedtuple is  : ")
# S as a namedTuple
print(S)
# S as a normal dictionary
print(S._asdict())


 
```