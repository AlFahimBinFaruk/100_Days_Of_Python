def one_decorator(func):
    print("one_decorator")

    def inner():
        x = func()
        x = x * 3
        print("Final result : ", x)

    return inner


def two_decorator(func):
    print("two_decorator")

    def inner():
        x = func()
        x = x * 2
        return x

    return inner


# At first, it will call  one_decorator then it will call two_decorator then that will call sum
# working logic is more like last in first out.

@one_decorator
@two_decorator
def sum():
    print("calling sum")
    return 10


sum()
