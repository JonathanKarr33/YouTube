# calculate total in list
list_of_numbers = [3,4,2,76,13]
#total = 0
#for item in list_of_numbers:
#    total += item
total = sum(item for item in list_of_numbers)
total = sum(list_of_numbers)
print(total)

# multiply items in list by 2
original_list = [1,2,3,4,5]
#multiplied_list = []
#for item in original_list:
#    multiplied_list.append(item * 2)
multiplied_list = [item * 2 for item in original_list]
print(multiplied_list)