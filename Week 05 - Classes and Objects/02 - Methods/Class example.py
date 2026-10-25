class Student:
    def __init__(self,name,program,marks):
        self.name=name
        self.program=program
        self.marks=marks
students=[]
with open("Studentdata.txt","r") as file:
    for line in file:
        name,program,marks=line.strip().split(",")
        s=Student(name,program,int(marks))
        students.append(s)

print("STUDENTS DETAILS")
print("---------------------------------")
for student in students:
    print("Name:",student.name)
    print("Program:",student.program)
    print("Mark:",student.marks)
    print("------------------------------------")

print("Total students:",len(students))
