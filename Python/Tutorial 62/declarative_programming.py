numbers = list(range(50))
#filtered_list = []
#for number in numbers:
#    if number % 3 == 0 and number % 5 == 0:
#        filtered_list.append(number)
filtered_list = list(filter(lambda x : x % 3 == 0 and x % 5 ==0,numbers))
print(filtered_list)

#cubed = []
#for number in numbers:
#    if number % 10 == 0:
#        cubed.append(number ** 3)
cubed = [number ** 3 for number in numbers if number % 10 == 0]
print(cubed)