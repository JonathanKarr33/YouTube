def sum(a,b):
    return a+b
sum(3,4)
print(sum(3,4))
a = sum(3,4)
print(a)
def divison_with_default_parameters(a,b=1):
    if (b==0):
        return "Cannot divide by zero"
    return a/b
print(divison_with_default_parameters(2,0))
print(divison_with_default_parameters(2,2))
print(divison_with_default_parameters(3))
print(divison_with_default_parameters())