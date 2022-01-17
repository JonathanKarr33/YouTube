def filter_list_to_power(power:int, divisor:int, number_of_values:int) -> list:
    """
    This takes in a list of a range of numbers starting at zero
    and returns a filtered list to a given power for the numbers
    divisible by the divisors
    
    Args:
        power (int) : the power that it is being raised to
        divisor (int) : what is checked to see if the number is divisible by
        number_of_values (int) : the length of the numbers list
    Returns:
        filtered_list (list) :the list of filtered values
    """
    numbers = list(range(number_of_values))
    filtered_list = [number ** power for number in numbers if number % divisor == 0]
    return filtered_list
print(filter_list_to_power(3,6,60))