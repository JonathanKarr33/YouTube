def power(n):
    for i in range(1000000):
        yield n**i
answer = power(3)
print(next(answer))
print(next(answer))
print(next(answer))