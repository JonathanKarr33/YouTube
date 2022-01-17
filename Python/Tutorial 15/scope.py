def add (a,b):
    c = a + b
    return c
a = 77
print(add(1,2))
# print(c) doesn't work because of scope
def subtract (d,e):
    global f
    f = d - e
    return f
subtract(1,2)
print(f)