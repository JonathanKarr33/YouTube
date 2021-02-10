prime_numbers = [2]
num = 3
while num < 1000:
    for i in range (2,num):
        if num % i == 0:
            break
        elif i == num-1:
            prime_numbers.append(num)
    num +=1
print(prime_numbers)