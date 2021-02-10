num = int(input("Enter a number to see if it is prime: "))
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(str(num) + " is not a prime number")
            break
    else:
        print(str(num) + " is a prime number")
else:
    print("You must enter a number greater than one")