def is_prime (num):
    if (num < 1):
        return "Invalid number"
    for i in range(2,num):
        if(((num/i)%i) == 0):
            return False
    return True
ask = int(input("Enter a positive integer: "))
answer = is_prime(ask)
print(answer)