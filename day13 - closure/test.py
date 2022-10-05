text = "suhan"
def outerFunction(text):
    text = text

    def innerFunction(text):
        text = text
        print(text)

    innerFunction("Zayn")

    print(text)

outerFunction("fahim")
