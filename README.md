# Education Service CLI

A command-line interface (CLI) application for managing students and teachers for an educational service. The application connects to a MongoDB database to store and retrieve user information, allowing for dynamic assignment of teachers to students and collaboration between teachers.

## About The Project

This project is a simple console-based application built with Python that serves two types of users: students and teachers. It uses a MongoDB backend to manage data.

### Features

- **Dual User Roles**: Separate workflows for Students and Teachers.
- **Student Services**:
  - Register for a lesson in a specific subject (Maths, Physics, Chemistry, or Biology).
  - Select a lesson duration.
  - Get automatically assigned an available teacher for the chosen subject.
  - Receive a cost calculation for the lesson.
- **Teacher Services**:
  - Register as a new teacher for a specific subject.
  - Find another teacher to collaborate with in a specific subject.
- **Database Integration**: All student and teacher data is persisted in a MongoDB database.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Make sure you have the following installed:

- **Python 3**: The script is written in Python. You can download it from [python.org](https://www.python.org/downloads/).
- **MongoDB**: The application requires a running MongoDB instance. You can find installation instructions on the [official MongoDB website](https://www.mongodb.com/try/download/community).
- **pip**: Python's package installer, which usually comes with Python.

### Installation

1.  **Get the code**
    If this were a Git repository, you would clone it. For now, simply place the `main.py` file in your project directory.

2.  **Install Python dependencies**
    This project requires the `pymongo` library to connect to MongoDB. Install it using pip:

    ```sh
    pip install pymongo
    ```

3.  **Set up the Database**
    The script connects to a local MongoDB instance by default (`mongodb://127.0.0.1:27017/`).
    - Ensure your MongoDB server is running.
    - The script will automatically create the `schooldb` database and the `students` and `teachers` collections when you first run it.

4.  **Seed the Database with Teachers**
    For the student and teacher collaboration features to work, you must have some teachers in the database. Connect to your MongoDB instance (using `mongosh` or a GUI like MongoDB Compass) and add some initial teacher documents.

    First, select the database:

    ```javascript
    use schooldb;
    ```

    Then, insert a few teachers into the `teachers` collection:

    ```javascript
    db.teachers.insertMany([
      { name: "Albert Einstein", subject: "Physics" },
      { name: "Marie Curie", subject: "Chemistry" },
      { name: "Isaac Newton", subject: "Maths" },
      { name: "Charles Darwin", subject: "Biology" },
    ]);
    ```

## How to Use

Run the application from your terminal:

```sh
python main.py
```

The application will prompt you to identify as a student or a teacher.

### Student Workflow

1.  Enter `S` when prompted.
2.  Enter your full name.
3.  Choose a subject from the list (e.g., `1` for Maths).
4.  Select the desired lesson duration.
5.  The application will confirm your booking, assign you a teacher, and display the total cost. Your name will be saved to the database.

### Teacher Workflow

1.  Enter `T` when prompted.
2.  Enter your full name.
3.  Choose your goal:
    - **Teach (Option 1)**:
      - Select the subject you will teach.
      - Your details will be added to the `teachers` collection, making you available for student assignments and collaborations.
    - **Collaborate (Option 2)**:
      - Select the subject for collaboration.
      - The system will assign you a random fellow teacher from that subject to collaborate with.

### Quitting the Application

At most prompts, you can enter `q` or `0` to exit the application.

### Collaborators
- Austin Muchai
- Melanie Thiong'oh
- Mathews Kipruto
- 
