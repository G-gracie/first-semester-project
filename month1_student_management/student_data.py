students = []

def add_student():
    """Collect student info from the user and add it to the students list."""
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = float(input("Enter student grade (0–100): "))
    student = {"name": name, "age": age, "grade": grade}
    students.append(student)
    print(f"Student {name} added successfully!\n")


def view_students():
    """Display all students in the list."""
    if not students:
        print("No students found.\n")
        return

    print("\n--- Student List ---")
    for i, student in enumerate(students, 1):
        print(f"{i}. Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
    print()  # Move print() outside the loop


def get_average_grade():
    """Calculate and return the average grade of all students."""
    if not students:
        return 0.0

    total = sum(student["grade"] for student in students)
    return total / len(students)
