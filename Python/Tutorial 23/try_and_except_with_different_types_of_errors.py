try:
    print("Enter 2 number to divide")
    num1 = float(input("What is the first number: "))
    num2 = float(input("What is the second number: "))
    print(num1/num2)
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("You must enter a number")
except:
    print("There was another type of error")
finally:
    print("This will run no matter what")