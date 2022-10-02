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


