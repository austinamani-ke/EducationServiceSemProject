# Importing the python random functionality
import random
# Importing Mongo DB functionality
from pymongo import MongoClient
# Importing the database
client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000")

# Initializing the database
db = client.schooldb

# Initializing the collections
students = db.students
teachers = db.teachers

# Converting the collections into lists for easier use in python
mathsTeachers = list(teachers.find({"subject": "Maths"}))
physicsTeachers = list(teachers.find({"subject": "Physics"}))
chemistryTeachers = list(teachers.find({"subject": "Chemistry"}))
biologyTeachers = list(teachers.find({"subject": "Biology"}))

# Initializing variables
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

# Prompting for user status
status = input("Greetings, are you a student or a teacher?(S for student T for teacher)(q to quit): ")
while True:  

    # Terminating the program if required
    if status.upper() == 'Q':
        break

    # Receiving the student name and checking that it does not contain any numbers or symbols
    if status.upper() == 'S':
        studentName = input("Enter your full name: (q to quit)")
        studentHasDigit = any(char.isdigit() for char in studentName)
        studentHasSymbol = any(not char.isalnum() and not char.isspace() for char in studentName)

        # Terminating if the name contains numbers or symbols
        if studentHasDigit or studentHasSymbol:
            print("Your name cannot contain numbers or symbols. Please restart the process")
            break

        # Terminating the program if required
        if studentName.upper() == "Q":
            break

        # Checking that the name is not an empty string
        if studentName == '':
            print("Please enter a valid name")
            break
        
        # Prompting for the subject the student want to learn
        subject = input("What subject are you taking?(0 to quit)\n 1: Maths\n 2: Physics\n 3: Chemistry\n 4: Biology\n Which one? ")
        match subject:
            case "0":
                break # Terminating the program if required
            case "1":
                subjectTaken = "Maths"
                assignedTeacher = random.choice(mathsTeachers) # Assigning the student a teacher for their subject
                assignedTeacherName = assignedTeacher["name"] 
            case "2":
                subjectTaken = "Physics"
                assignedTeacher = random.choice(physicsTeachers) # Assigning the student a teacher for their subject
                assignedTeacherName = assignedTeacher["name"]
            case "3":
                subjectTaken = "Chemistry"
                assignedTeacher = random.choice(chemistryTeachers) # Assigning the student a teacher for their subject
                assignedTeacherName = assignedTeacher["name"]
            case "4":
                subjectTaken = "Biology"
                assignedTeacher = random.choice(biologyTeachers) # Assigning the student a teacher for their subject
                assignedTeacherName = assignedTeacher["name"]
            case _:
                print("Invalid input. Please restart and input something valid.") 
                break # Terminating the program if any other input that is not valid is entered

        # Prompting the student to input the duration of their lesson
        lessonDuration = input("How long do you want the lesson to be?(0 to quit)\n 1: 30 Minutes\n 2: 1 Hour\n 3: 1 and a Half Hours \n 4: 2 Hours \n Select an Option: ")
        match lessonDuration:
            case "0":
                break # Terminating the program if required
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
                break # Terminating the program if invalid input is entered

        # Calculating costs according to subject and duration
        if subjectTaken == "Maths":
            totalCost = costMaths * durationMinutes
            totalCost = round(totalCost)
        elif subjectTaken == "Physics" or subjectTaken == "Chemistry" or subjectTaken == "Biology":
            totalCost = costSubject * durationMinutes
            totalCost = round(totalCost)

        # Finally adding the student to the database and displaying the final message
        db.students.insert_one({"name": studentName})
        print(f"Hello {studentName}! Your assigned teacher for your {durationMinutes} minutes of {subjectTaken} is {assignedTeacherName}. Your cost is going to be {totalCost} shillings.")
        break #Terminating the program

    # Receiving the teacher name and checking that it does not contain numbers or symbols
    elif status.upper() == "T":
        teacherName = input("Enter your full name: (q to quit)")
        teacherHasDigit = any(char.isdigit() for char in teacherName)
        teacherHasSymbol = any(not char.isalnum() and not char.isspace() for char in teacherName)

        # Terminating the program if the teacher name contains numbers or symbols
        if teacherHasDigit or teacherHasSymbol:
            print("Your name cannot contain numbers or symbols. Please restart the process")
            break

        # Terminating the program if requried
        if teacherName.upper() == "Q":
            break
        
        # Checking that the teacher name is not an empty string
        if teacherName == '':
            print("Please enter a valid name")
            break
        
        # Creating a custom error solution
        class InvalidRoleError(Exception):
            pass

        # Prompting the teacher for whether they want to teach or collaborate
        userInput = input("What do you want to achieve?(0 to quit)\n 1: Teach\n 2: Collaborate\n")

        # Checking that the role input is not a string
        try:
            if userInput == '':
                raise InvalidRoleError("Please enter a valid role")
            
            # Converting the role input type into an integer
            role = int(userInput)

            # Terminating the program if required
            if role == 0:
                break
            elif role not in (1, 2):
                raise InvalidRoleError("Chose either 1 or 2") # Checking that the input is between only 1 and 2
            
        except InvalidRoleError as e:
            print(e)
        except ValueError:
            raise InvalidRoleError("That is not a valid number") from None # Raising an error if the input is not 1 or 2
            
        # Prompting the teacher for the subject they teach
        if role == 1:
            subject = input("What subject are you teaching?(0 to quit)\n 1: Maths\n 2: Physics\n 3: Chemistry\n 4: Biology\n Which one? ")
            match subject:
                case "0":
                    break # Terminating the program if required
                case "1":
                    subjectTaught = "Maths"
                    # Adding the teacher to the database and welcoming them
                    mathsTeachers.append(teacherName) 
                    db.teachers.insert_one({"name": teacherName , "subject": subjectTaught})
                    print(f"Welcome {teacherName}!")
                case "2":
                    subjectTaught = "Physics"
                    # Adding the teacher to the database and welcoming them
                    physicsTeachers.append(teacherName)
                    db.teachers.insert_one({"name": teacherName , "subject": subjectTaught})
                    print(f"Welcome {teacherName}!")
                case "3":
                    subjectTaught = "Chemistry"
                    # Adding the teacher to the database and welcoming them
                    chemistryTeachers.append(teacherName)
                    db.teachers.insert_one({"name": teacherName , "subject": subjectTaught})
                    print(f"Welcome {teacherName}!")
                case "4":
                    subjectTaught = "Biology" 
                    # Adding the teacher to the database and welcoming them
                    biologyTeachers.append(teacherName)
                    db.teachers.insert_one({"name": teacherName , "subject": subjectTaught})
                    print(f"Welcome {teacherName}!")
                case _:
                    print("Invalid input. Please restart and input something valid.")  
                    break # Terminating the program if the input is invalid
            break   

        # Prompting the teacher for the subject they want to collaborate for
        elif role == 2:
            subjectCollaborate = input("What subject do want to collaborate for?(0 to quit)\n 1: Maths\n 2: Physics\n 3: Chemistry\n 4: Biology\n Which One? ")
            match subjectCollaborate:
                case "0":
                    break # Prompting the program if required
                case "1":
                    # Assigning the teacher a collaboration partner
                    assignedCollaborator = random.choice(mathsTeachers)
                    assignedCollaboratorName = assignedCollaborator["name"]
                    print(f"You will be collaborating with {assignedCollaboratorName}")
                case "2":
                    # Assigning the teacher a collaboration partner
                    assignedCollaborator = random.choice(physicsTeachers)
                    assignedCollaboratorName = assignedCollaborator["name"]
                    print(f"You will be collaborating with {assignedCollaboratorName}")
                case "3":
                    # Assigning the teacher a collaboration partner
                    assignedCollaborator = random.choice(chemistryTeachers)
                    assignedCollaboratorName = assignedCollaborator["name"]
                    print(f"You will be collaborating with {assignedCollaboratorName}")
                case "4":
                    # Assigning the teacher a collaboration partner
                    assignedCollaborator = random.choice(biologyTeachers)
                    assignedCollaboratorName = assignedCollaborator["name"]
                    print(f"You will be collaborating with {assignedCollaboratorName}")
                case _:
                    print("Invalid input. Please restart and input something vaild.")
                    break # Terminating the program if inout is invalid
            break

    if status.upper() != 'Q' or status.upper() != 'S' or status.upper() != 'T':
        print("Invalid input. Please restart and input something valid.")
        break # Terminating the program if the input is invalid.


# print(mathsTeachers)
# for teacher in teachers.find():
#     print(teacher)
