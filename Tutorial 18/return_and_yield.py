def sum (a,b):
    return a + b
    print("This won't print")
#print(sum(3,4))
def loop (num):
    for i in range(num):
        yield i
        print("test")
print(loop(3))
print(list(loop(3)))
count = loop(3)
print(next(count))
print(next(count))
print(next(count))
print(next(count))