def outer_function(text):
    def inner_function():
        print(text)
    inner_function()
outer_function("Hello world")

def pop(list1):
    def get_last_element(list2):
        return list1[len(list2)-1]
    list1.remove(get_last_element(list1))
    print (list1)
    return (list1)
list_of_numbers = [1,2,3,4,5,6]
pop(list_of_numbers)
pop(list_of_numbers)