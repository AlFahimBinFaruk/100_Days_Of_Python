# the best way to work with file system in Python is "with" statement
# read
with open("G:\\100DaysOfPython\\day05\\file_system\\sample3.txt","r") as f:
    a=f.read().lower()
print("Data",a)

# write
with open("G:\\100DaysOfPython\\day05\\file_system\\sample3.txt","w") as f:
    f.write("Overwritten")

# append
with open("G:\\100DaysOfPython\\day05\\file_system\\sample3.txt","a") as f:
    f.write("overwritten")