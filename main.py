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
role = 0
subjectTaught = ''
subjectCollaborate = 0
assignedCollaborator = '' 
assignedCollaboratorName = ''

costMaths = 25
costSubject = 16.67
totalCost = 0

status = input("Greetings, are you a student or a teacher?(S for student T for teacher)(q to quit): ")
while True:  

    if status.upper() == 'Q':
        break

    if status.upper() == 'S':
        studentName = input("Enter your full name: (q to quit)")
        studentHasDigit = any(char.isdigit() for char in studentName)
        studentHasSymbol = any(not char.isalnum() and not char.isspace() for char in studentName)

        if studentHasDigit or studentHasSymbol:
            print("Your name cannot contain numbers or symbols. Please restart the process")
            break

        if studentName.upper() == "Q":
            break

        if studentName == '':
            print("Please enter a valid name")
            break
        
        subject = input("What subject are you taking?(0 to quit)\n 1: Maths\n 2: Physics\n 3: Chemistry\n 4: Biology\n Which one? ")
        match subject:
            case "0":
                break
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
                print("Invalid input. Please restart and input something valid.")
                break

        lessonDuration = input("How long do you want the lesson to be?(0 to quit)\n 1: 30 Minutes\n 2: 1 Hour\n 3: 1 and a Half Hours \n 4: 2 Hours \n Select an Option: ")
        match lessonDuration:
            case "0":
                break
            case "1":
                durationMinutes = 30
            case "2":
                durationMinutes = 60
            case "3":
                durationMinutes = 90
            case "4":
                durationMinutes = 120
            case _:
                print("Invalid Input. Please restart and input something valid.")
                break

        if subjectTaken == "Maths":
            totalCost = costMaths * durationMinutes
            totalCost = round(totalCost)
        elif subjectTaken == "Physics" or subjectTaken == "Chemistry" or subjectTaken == "Biology":
            totalCost = costSubject * durationMinutes
            totalCost = round(totalCost)

        db.students.insert_one({"name": studentName})
        print(f"Hello {studentName}! Your assigned teacher for your {durationMinutes} minutes of {subjectTaken} is {assignedTeacherName}. Your cost is going to be {totalCost} shillings.")
        break

    elif status.upper() == "T":
        teacherName = input("Enter your full name: (q to quit)")
        teacherHasDigit = any(char.isdigit() for char in teacherName)
        teacherHasSymbol = any(not char.isalnum() and not char.isspace() for char in teacherName)

        if teacherHasDigit or teacherHasSymbol:
            print("Your name cannot contain numbers or symbols. Please restart the process")
            break

        if teacherName.upper() == "Q":
            break
        
        if teacherName == '':
            print("Please enter a valid name")
            break

        class InvalidRoleError(Exception):
            pass

        userInput = input("What do you want to achieve?(0 to quit)\n 1: Teach\n 2: Collaborate\n")

        try:
            if userInput == '':
                raise InvalidRoleError("Please enter a valid role")
            
            role = int(userInput)

            if role == 0:
                break
            elif role not in (1, 2):
                raise InvalidRoleError("Chose either 1 or 2")
            
        except InvalidRoleError as e:
            print(e)
        except ValueError:
            raise InvalidRoleError("That is not a valid number") from None
            

        if role == 1:
            subject = input("What subject are you teaching?(0 to quit)\n 1: Maths\n 2: Physics\n 3: Chemistry\n 4: Biology\n Which one? ")
            match subject:
                case "0":
                    break
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
                    print("Invalid input. Please restart and input something valid.")  
                    break
            break   
        elif role == 2:
            subjectCollaborate = input("What subject do want to collaborate for?(0 to quit)\n 1: Maths\n 2: Physics\n 3: Chemistry\n 4: Biology\n Which One? ")
            match subjectCollaborate:
                case "0":
                    break
                case "1":
                    assignedCollaborator = random.choice(mathsTeachers)
                    assignedCollaboratorName = assignedCollaborator["name"]
                    print(f"You will be collaborating with {assignedCollaboratorName}")
                case "2":
                    assignedCollaborator = random.choice(physicsTeachers)
                    assignedCollaboratorName = assignedCollaborator["name"]
                    print(f"You will be collaborating with {assignedCollaboratorName}")
                case "3":
                    assignedCollaborator = random.choice(chemistryTeachers)
                    assignedCollaboratorName = assignedCollaborator["name"]
                    print(f"You will be collaborating with {assignedCollaboratorName}")
                case "4":
                    assignedCollaborator = random.choice(biologyTeachers)
                    assignedCollaboratorName = assignedCollaborator["name"]
                    print(f"You will be collaborating with {assignedCollaboratorName}")
                case _:
                    print("Invalid input. Please restart and input something vaild.")
                    break
            break

    if status.upper() != 'Q' or status.upper() != 'S' or status.upper() != 'T':
        print("Invalid input. Please restart and input something valid.")
        break


# print(mathsTeachers)
# for teacher in teachers.find():
#     print(teacher)
