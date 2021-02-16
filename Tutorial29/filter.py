from statistics import mean
data = [33,54,1,-4,706,54,456]
average = mean(data)
print(list(filter(lambda x: x<average,data)))