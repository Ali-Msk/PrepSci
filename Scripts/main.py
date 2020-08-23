from Tutor import *
from Student import *
import time
tutors = []
students = []
subjects = ["Math", "Calculus", "History", "Science", "Chem", "Physics", "Biology", "English", "French"]


def adTutor():
    newTutor = Tutor(input("Enter tutor name: "))
    age = input("Enter Age: ")
    if(age != -1):
        newTutor.age = age

    #newTutor.degrees
    while(degree != "-1"):
        degree = input("Enter Age:    -1 to stop")
        if (degree != -1):
            newTutor.degrees.insert(degree)



def findTutors( student: Student) -> [Tutor]:
    possibleTutors = []
    for i in Tutors:
        if(i.maxGradeToTeach >= student.grade and i.minxGradeToTeach <= student.grade):
            subjectMatch = False
            for j in student.subjects:
                if(j in i.subjects):
                    subjectMatch  = True

            if(subjectMatch):
                possibleTutors.insert(i)

def printHardCode():
    student = input("Please enter player name: ")
    subject = input("Enter subject: ")
    grade = input("Enter grade: ")

    print ("Searching for matches...")
   ## sleep(1000)
    print ("Here is your list of matches")
    print ("-----------------------------------------------------------------------------------------")
    print ("Hakeem Kirk  ******")
   ## print ("    Rating:   ***** ")
    print ("    Distance:   ~ 5km ")
    print ("    Sessions Taught: 432 ")
    print ("    Experience Teachign: 11 years ")
    print ("    Main Subjects:   Calculus, Statistics, Dynamics, Computer Porgamming")
  #  print(" ")
    print ("-----------------------------------------------------------------------------------------")
    print("Savanna Whitaker  *****")
    print ("    Distance:   ~ 7km ")
    print ("    Sessions Taught: 1222 ")
    print ("    Experience Teaching: 21 years ")
    print ("    Main Subjects:   Calculus, Organic Chemistry, Statistics, Molecules and Materials")
   # print(" ")
    print ("-----------------------------------------------------------------------------------------")
    print("Benny Holt  ****")
    print ("    Distance:   <1km ")
    print ("    Sessions Taught: 99 ")
    print ("    Experience Teaching: 4 years ")
    print ("    Main Subjects:   Calculus")
  #  print(" ")
    print ("-----------------------------------------------------------------------------------------")
    print("Gruffydd Marquez  ****")
    print ("    Distance:   ~ 3 km ")
    print ("    Sessions Taught: 432 ")
    print ("    Experience Teaching: 5 years ")
    print ("    Main Subjects:   Calculus, Statistics")
#    print(" ")
    print ("-----------------------------------------------------------------------------------------")
    print("Kaila Salman  ***")
    print ("    Distance:   <5km ")
    print ("    Sessions Taught: 12 ")
    print ("    Experience Teaching: <1 years ")
    print ("    Main Subjects:   Calculus, Computer Porgamming")
   ## print(" ")
    print ("-----------------------------------------------------------------------------------------")

if __name__ == "__main__":
    printHardCode()