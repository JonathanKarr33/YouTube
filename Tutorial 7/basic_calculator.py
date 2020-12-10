print("Enter a number, operator, and another number")
num1 = float(input("What is the first number: "))
op =input("What is the operator symbol: ")
num2 = float(input("What is the second number: "))
if (op=="+"):
    print(num1+num2)
elif (op=="-"):
    print(num1-num2)
elif (op=="*"):
    print(num1*num2)
elif (op=="/"):
    print(num1/num2)
elif (op=="//"):
    print(num1//num2)
elif (op=="%"):
    print(num1%num2)
elif (op=="**"):
    print(num1**num2)
else:
    print("Invalid operator")