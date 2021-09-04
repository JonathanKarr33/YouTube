from enum import Enum, auto

class grade(Enum):
    freshman = 9
    sophomore = 10
    junior = 11
    senior = auto()
print(grade.freshman.name)
print(grade.freshman.value)
print(grade.senior.value)