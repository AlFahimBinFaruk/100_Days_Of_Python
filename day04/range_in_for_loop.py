# by default it will start from 0
for i in range(10):
    print("i is =>", i)

print("Done")

# now it will start from 1
for j in range(1, 10):
    print("j is =>", j)

print("Done")

# range in for loop with step size
'''
1 is start - first argument(by default 0)
10 is stop - second arg
2 is step size - third arg(by default 1)
'''
for k in range(1, 10, 2):
    print("K is =>", k)
