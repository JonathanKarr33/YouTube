def outer_function(text):
    def inner_function():
        print(text)
    return inner_function
my_func = outer_function("Hello world")
del outer_function
my_func ()

def power(exponent):
    def power_of(base):
        return pow(base,exponent)
    return power_of
cube = power(3)
print(cube(2))
print(cube(3))
print(cube(4))
print(cube(5))