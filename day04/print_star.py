n = 6
for i in range(6):
    print(" " * (n - i - 1), end="")
    print("*" * (2 * i + 1), end="")
    print(" " * (n - i - 1))
