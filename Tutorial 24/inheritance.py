from classes_with_methods import student
class high_school_or_college_student(student):
    def year(self):
        if (self.grade == (9 or 13)):
            return "Freshman"
        elif(self.grade == (10 or 14)):
            return "Sophomore"
        elif(self.grade == (11 or 15)):
            return "Junior"
        elif(self.grade == (12 or 16)):
            return "Senior"
        else:
            return False
student1 = high_school_or_college_student("Blake",12,4.12)
print(student1.year())
print(student1.honors())