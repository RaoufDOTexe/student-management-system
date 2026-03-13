import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
age INTEGER,
major TEXT
)
""")

conn.commit()

def add_student():
    name = input("Name: ")
    age = input("Age: ")
    major = input("Major: ")

    cursor.execute(
        "INSERT INTO students (name, age, major) VALUES (?, ?, ?)",
        (name, age, major)
    )

    conn.commit()
    print("Student added")


def view_students():

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    for student in students:
        print(student)


def delete_student():

    student_id = input("Student ID to delete: ")

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    conn.commit()

    print("Student deleted")


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
