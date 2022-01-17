def positive_subtraction(func):
    def inner (a,b):
        if a < b:
            a,b = b,a
        return func(a,b)
    return inner
@positive_subtraction
def subtraction(a,b):
    return a - b
print(subtraction(8,7))