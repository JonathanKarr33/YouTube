students = ["Mike H", "James A", "John B", "Abby V", "Emily R, Joe T"]
students.sort(key = lambda name : name.split(" ")[-1].lower())
print(students)