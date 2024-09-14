
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)
        print(f"Grade {grade} added for {self.name}.")

    def print_grades(self):
        print(f"Grades for {self.name}: {self.grades}")

class GradeBook:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        if name not in self.students:
            self.students[name] = Student(name)
            print(f"Student {name} added.")
        else:
            print(f"Student {name} already exists.")

    def add_grade(self, name, grade):
        if name in self.students:
            self.students[name].add_grade(grade)
        else:
            print(f"Student {name} not found. Please add the student first.")

    def print_grades(self, name):
        if name in self.students:
            self.students[name].print_grades()
        else:
            print(f"Student {name} not found.")

def main():
    gradebook = GradeBook()
    while True:
        action = input("Choose an action: add student, add grade, print grades, or exit: ").strip().lower()
        if action == "add student":
            name = input("Enter student name: ").strip()
            gradebook.add_student(name)
        elif action == "add grade":
            name = input("Enter student name: ").strip()
            grade = input("Enter grade: ").strip()
            gradebook.add_grade(name, grade)
        elif action == "print grades":
            name = input("Enter student name: ").strip()
            gradebook.print_grades(name)
        elif action == "exit":
            break
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()