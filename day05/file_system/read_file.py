# read file in python
# you have to provide full path name of that file you want to read
# by default the mode is r =read
file = open('G:\\100DaysOfPython\\day04\\file_system\\sample.txt', 'r')

'''read full file'''
#data = file.read()
'''read only 5 lines'''
data = file.read(5)
print(data)

file.close()
'''read a file line by line'''
file2 = open('G:\\100DaysOfPython\\day04\\file_system\\sample.txt', 'r')
lineOne = file2.readline()
lineTwo = file2.readline()
print("Line one", lineOne)
print("Line twi", lineTwo)
