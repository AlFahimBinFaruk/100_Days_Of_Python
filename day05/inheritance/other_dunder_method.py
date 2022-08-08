class Test:

    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f"number is {self.num}"


data = Test(3)
print(data)