class student:
    def __init__(self,name,grade,gpa):
        self.name = name
        self.grade = grade
        self.gpa = gpa
student1 = student("Eli",12,4.32)
student2 = student("Emilo",11,3.96)
print(student1.name)
print(student2.grade)