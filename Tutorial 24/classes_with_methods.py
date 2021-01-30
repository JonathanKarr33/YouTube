class student:
    def __init__(self,name,grade,gpa):
        self.name = name
        self.grade = grade
        self.gpa = gpa
    def honors(self):
        if (self.gpa >= 4.0):
            return "Highest Honors"
        elif (self.gpa >= 3.75):
            return "High Honors"
        elif (self.gpa >= 3.5):
            return "Honors"
        else:
            return None
student1 = student("Eli",12,4.32)
student2 = student("Emilo",11,3.96)
#print(student1.name)
#print(student2.honors())
