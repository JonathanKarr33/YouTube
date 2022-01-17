prime_numbers = [2]
num = 3
while num < 1000:
    for i in range (len(prime_numbers)):
        if num % prime_numbers[i] == 0:
            break
        elif prime_numbers[i] == prime_numbers[(len(prime_numbers)-1)]:
            prime_numbers.append(num)
    num +=1
print(prime_numbers)