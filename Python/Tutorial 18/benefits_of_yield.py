def squares(number):
    squared = []
    for i in range (len(number)):
        squared.append(number[i]**2)
    return squared
print(squares([3,2,5,8]))
def squares_using_yield(number):
    for i in range (len(number)):
        yield number[i]**2
print(list(squares_using_yield([3,2,5,8])))