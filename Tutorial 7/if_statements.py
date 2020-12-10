print("Enter 3 numbers to see what is the largest")
num1 = (float(input("Input the first number: ")))
num2 = (float(input("Input the first number: ")))
num3 = (float(input("Input the first number: ")))
if (num1>=num2 and num1>=num3):
    print(str(num1) +" is the largest number")
elif (num2>=num1 and num2>=num3):
    print(str(num2) +" is the largest number")
else:
    print(str(num3) +" is the largest number")