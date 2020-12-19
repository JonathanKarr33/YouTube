user_name = input("What is your name: ")
user_name = user_name.upper()
name = ""
for letter in user_name:
    if letter in "AEIOU":
        break
    name+=letter
print(name)