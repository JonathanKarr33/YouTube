def square(n):
    a = n * n
    yield a
    yield 1000
answer = square(3)
print(next(answer))
print(next(answer))
#print(next(answer))
answer2 = square(4)
for i in answer2:
    print(i)