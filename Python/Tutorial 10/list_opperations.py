list_1 = [3,7,6,5,3]
list_2 = list_1[0:-1]
print(list_1,list_2)
list_2 = list_1[:]
print(list_1,list_2)
list_2.append(33)
print(list_1,list_2)
list_2 = list_1
print(list_1,list_2)
list_2.append(27)
print(list_1,list_2)