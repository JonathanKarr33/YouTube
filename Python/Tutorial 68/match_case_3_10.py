x = int(input("Enter an integer: "))
match x:
    case 1:
        print("hello")
    case 2:
        print("world")
    case _:
        print("You didn't enter 1 or 2")