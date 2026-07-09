import random
from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000")

db = client.schooldb

students = db.students
teachers = db.teachers

mathsTeachers = list(teachers.find({"subject": "Maths"}))
physicsTeachers = list(teachers.find({"subject": "Physics"}))
chemistryTeachers = list(teachers.find({"subject": "Chemistry"}))
biologyTeachers = list(teachers.find({"subject": "Biology"}))

studentName = ''
subjectTaken = ''
durationMinutes = 0
assignedTeacher = ''
assignedTeacherName = ''

teacherName = ''
subjectTaught = ''

costMaths = 25
costSubject = 16.67
totalCost = 0

status = input("Greetings, are you a student or a teacher(S for student T for teacher): ")

if status.upper() == 'S':
    studentName = input("Enter your full name: ")
    db.students.insert_one({"name": studentName})
    subject = input("What subject are you taking?\n 1: Maths\n 2: Physics\n 3: Chemistry\n 4: Biology\n Which one? ")
    match subject:
        case "1":
            subjectTaken = "Maths"
            assignedTeacher = random.choice(mathsTeachers)
            assignedTeacherName = assignedTeacher["name"] 
        case "2":
            subjectTaken = "Physics"
            assignedTeacher = random.choice(physicsTeachers)
            assignedTeacherName = assignedTeacher["name"]
        case "3":
            subjectTaken = "Chemistry"
            assignedTeacher = random.choice(chemistryTeachers)
            assignedTeacherName = assignedTeacher["name"]
        case "4":
            subjectTaken = "Biology"
            assignedTeacher = random.choice(biologyTeachers) 
            assignedTeacherName = assignedTeacher["name"]
        case _:
            print("Subject unavailable for now")

    lessonDuration = input("How long do you want the lesson to be?\n 1: 30 Minutes\n 2: 1 Hour\n 3: 1 and a Half Hours \n 4: 2 Hours \n Select an Option: ")
    match lessonDuration:
        case "1":
            durationMinutes = 30
        case "2":
            durationMinutes = 60
        case "3":
            durationMinutes = 90
        case "4":
            durationMinutes = 120
        case _:
            print("Invalid Input!")

    if subjectTaken == "Maths":
        totalCost = costMaths * durationMinutes
        totalCost = round(totalCost)
    elif subjectTaken == "Physics" or subjectTaken == "Chemistry" or subjectTaken == "Biology":
        totalCost = costSubject * durationMinutes
        totalCost = round(totalCost)

    print(f"Hello {studentName}! Your assigned teacher for your {durationMinutes} minutes of {subjectTaken} is {assignedTeacherName}. Your cost is going to be {totalCost} shillings.")

elif status.upper() == "T":
    teacherName = input("Enter your full name: ")
    
    subject = input("What subject are you teaching?\n 1: Maths\n 2: Physics\n 3: Chemistry\n 4: Biology\n Which one? ")
    match subject:
        case "1":
            subjectTaught = "Maths"
            mathsTeachers.append(teacherName)
            db.teachers.insert_one({"name": teacherName , "subject": subjectTaught})
            print(f"Welcome {teacherName}!")
        case "2":
            subjectTaught = "Physics"
            physicsTeachers.append(teacherName)
            db.teachers.insert_one({"name": teacherName , "subject": subjectTaught})
            print(f"Welcome {teacherName}!")
        case "3":
            subjectTaught = "Chemistry"
            chemistryTeachers.append(teacherName)
            db.teachers.insert_one({"name": teacherName , "subject": subjectTaught})
            print(f"Welcome {teacherName}!")
        case "4":
            subjectTaught = "Biology" 
            biologyTeachers.append(teacherName)
            db.teachers.insert_one({"name": teacherName , "subject": subjectTaught})
            print(f"Welcome {teacherName}!")
        case _:
            print("Subject unavailable for now")  


# print(mathsTeachers)
# for teacher in teachers.find():
#     print(teacher)
