class Test:

    """
    01.Implement __repr__ for any class you implement. This should be second nature. Implement __str__ if you think it would be useful to have a string version which errs on the side of readability.
    02.Difference between __str__ and __repr__ : https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr
    """

    def __init__(self, num):
        self.num = num

    # def __str__(self):
    #     return f"number is {self.num}"

    def __repr__(self):
        return f"number is {self.num}"


data = Test(3)
print(data)