num_list = [1,2,3,6,9,20,30]

def calculate_result(x):
    return x**3 + 3*x**2

#result = [calculate_result(x) for x in num_list if calculate_result(x) < 300]
result = [result for x in num_list if (result := calculate_result(x)) < 300]
print(result)