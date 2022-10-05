# writing decorator function name like fahim_decorator is a good practice.

def fahim(func):

    def inner():
        func()
        print("fahim")

    # this return means calling inner function.
    return inner

@fahim
def suhan():
    print("suhan")

suhan()