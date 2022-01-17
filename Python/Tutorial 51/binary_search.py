def binary_search(list_of_items,item):
    start = 0
    end = len(list_of_items)-1

    while start <= end:
        midpoint = start + (end-start) // 2
        midpoint_value = list_of_items[midpoint]
        if midpoint_value == item:
            return midpoint
        elif item < midpoint:
            end = midpoint - 1
        else:
            start = midpoint + 1
    if list_of_items[0] == item:
        return 0
    else:
        return None

list1 = [1,2,2,3,7,8,9]
look = 1
print(binary_search(list1,look))