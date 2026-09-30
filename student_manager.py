import json
import os

DATA_FILE = "students.json"


def load_students():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_students(students):
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)


def add_student(students, name, admission_no, course):
    if not name or not admission_no or not course:
        return False, "All fields are required."

    for student in students:
        if student["admission_no"] == admission_no:
            return False, "Admission number already exists."

    students.append({
        "name": name,
        "admission_no": admission_no,
        "course": course
    })

    save_students(students)
    return True, "Student added successfully."


def search_student(students, admission_no):
    for student in students:
        if student["admission_no"] == admission_no:
            return student

    return None


def view_students(students):
    if not students:
        print("No students found.")
        return

    print("\nStudent Records")
    print("-" * 40)

    for student in students:
        print(f"Name: {student['name']}")
        print(f"Admission No: {student['admission_no']}")
        print(f"Course: {student['course']}")
        print("-" * 40)


def main():
    students = load_students()

    while True:
        print("\n=== Student Record Manager ===")
        print("1. Add student")
        print("2. View students")
        print("3. Search student")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Enter student name: ").strip()
            admission_no = input("Enter admission number: ").strip()
            course = input("Enter course: ").strip()

            success, message = add_student(
                students, name, admission_no, course
            )
            print(message)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            admission_no = input("Enter admission number: ").strip()
            student = search_student(students, admission_no)

            if student:
                print("\nStudent Found")
                print(f"Name: {student['name']}")
                print(f"Admission No: {student['admission_no']}")
                print(f"Course: {student['course']}")
            else:
                print("Student not found.")

        elif choice == "4":
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()
