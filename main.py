import sqlite3

# connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# create table if it does not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
major TEXT
)
""")

conn.commit()


# add student
def add_student():

    name = input("Name: ")
    age = input("Age: ")
    major = input("Major: ")

    cursor.execute(
        "INSERT INTO students (name, age, major) VALUES (?, ?, ?)",
        (name, age, major)
    )

    conn.commit()

    print("Student added successfully")


# view students
def view_students():

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    if not students:
        print("No students found")
        return

    print("\nID | Name | Age | Major")
    print("-" * 30)

    for student in students:
        print(f"{student[0]} | {student[1]} | {student[2]} | {student[3]}")


# search student
def search_student():

    name = input("Enter student name to search: ")

    cursor.execute(
        "SELECT * FROM students WHERE name LIKE ?",
        ('%' + name + '%',)
    )

    students = cursor.fetchall()

    if students:
        for student in students:
            print(student)
    else:
        print("Student not found")


# update student
def update_student():

    student_id = input("Enter student ID to update: ")

    name = input("New name: ")
    age = input("New age: ")
    major = input("New major: ")

    cursor.execute(
        "UPDATE students SET name = ?, age = ?, major = ? WHERE id = ?",
        (name, age, major, student_id)
    )

    conn.commit()

    print("Student updated successfully")


# delete student
def delete_student():

    student_id = input("Enter student ID to delete: ")

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    conn.commit()

    print("Student deleted successfully")


# main menu
while True:

    print("\n===== Student Management System =====")

    print("1 - Add Student")
    print("2 - View Students")
    print("3 - Search Student")
    print("4 - Update Student")
    print("5 - Delete Student")
    print("6 - Exit")

    choice = input("Select option: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Goodbye")
        break

    else:
        print("Invalid option")
