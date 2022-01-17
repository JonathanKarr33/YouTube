first_name = input("What is your first name: ")
last_name = input("What is your last name: ")
hello_world = lambda : "Hello world"
full_name = lambda first_name, last_name : first_name.strip().title() + " " + last_name.strip().title()
print(hello_world())
print(full_name(first_name,last_name))