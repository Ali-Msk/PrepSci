from Tutor import *
from Student import *
class main:
    tutors = []
    students = []
    subjects = ["Math", "Calculus", "History", "Science", "Chem", "Physics", "Biology", "English", "French"]
    if __name__ == "__main__":
        print ("hello world")



    def adTutor(self):
        newTutor = Tutor(input("Enter tutor name: "))
        age = input("Enter Age: ")
        if(age != -1):
            newTutor.age = age

        #newTutor.degrees
        while(degree != "-1"):
            degree = input("Enter Age:    -1 to stop")
            if (degree != -1):
                newTutor.degrees.insert(degree)



    def findTutors(self, student: Student) -> [Tutor]:
        possibleTutors = []
        for i in Tutors:
            if(i.maxGradeToTeach >= student.grade and i.minxGradeToTeach <= student.grade):
                subjectMatch = False
                for j in student.subjects:
                    if(j in i.subjects):
                        subjectMatch  = True

                if(subjectMatch):
                    possibleTutors.insert(i)