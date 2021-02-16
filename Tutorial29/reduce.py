from functools import reduce
numbers = [3,2,1,2]
power = lambda x,y: x**y
print(reduce(power,numbers))