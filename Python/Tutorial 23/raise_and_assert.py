try:
    print("Enter 2 number to divide")
    num1 = float(input("What is the first number: "))
    assert num1 > 0
    #raise ZeroDivisionError
    num2 = float(input("What is the second number: "))
    print(num1/num2)
except (ZeroDivisionError,ValueError):
    print("There was either a value or division error")
except:
    print("There was another type of error")
finally:
    print("This will run no matter what")