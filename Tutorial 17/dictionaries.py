phone_numbers = {"doctor":1234567890,"electrician":8000000011}
grades = dict(homework = 97, tests = 94, exam = 100)
print(phone_numbers)
print(grades)
print(phone_numbers["doctor"])
print(phone_numbers.get("Mom","This value doesn't exist"))
for key in phone_numbers.keys():
    print(key, "->", phone_numbers[key])
phone_numbers ["doctor"] = 8880000088
print(phone_numbers)
phone_numbers ["author"] = 4567890123
print(phone_numbers)
del phone_numbers["author"]
print(phone_numbers)
print(len(phone_numbers))
del phone_numbers
print(phone_numbers)