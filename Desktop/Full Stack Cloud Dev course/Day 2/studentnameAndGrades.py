grades = {}
def add_student(name):
    if name not in grades:
        grades[name] = []
        print(f"Student {name} added.")
    else:
        print(f"Student {name} already exists.")
def add_grade(name, grade):
    if name in grades:
        grades[name].append(grade)
        print(f"Grade {grade} added for {name}.")
    else:
        print(f"Student {name} not found. Please add the student first.")
def print_grades(name):
    if name in grades:
        print(f"Grades for {name}: {grades[name]}")
    else:
        print(f"Student {name} not found.")
def main():
    while True:
        action = input("Choose an action: add student, add grade, print grades, or exit: ").strip().lower()
        if action == "add student":
            name = input("Enter student name: ").strip()
            add_student(name)
        elif action == "add grade":
            name = input("Enter student name: ").strip()
            grade = input("Enter grade: ").strip()
            add_grade(name, grade)
        elif action == "print grades":
            name = input("Enter student name: ").strip()
            print_grades(name)
        elif action == "exit":
            break
        else:
            print("Invalid action. Please try again.")
if __name__ == "__main__":
    main()