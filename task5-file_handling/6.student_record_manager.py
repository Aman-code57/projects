class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self):
        student_id = input("Enter Student ID: ")
        if student_id in self.students:
            print("Student ID already exists.")
            return

        name = input("Enter Student Name: ")
        try:
            age = int(input("Enter Age: "))
        except ValueError:
            print("Invalid age.")
            return

        grade = input("Enter Grade (e.g., A, B+): ")

        self.students[student_id] = Student(student_id, name, age, grade)
        print("Student added successfully.")

    def view_all_students(self):
        if not self.students:
            print("No student records found.")
            return
        for student in self.students.values():
            print(student)

    def search_student(self):
        student_id = input("Enter Student ID to search: ")
        student = self.students.get(student_id)
        if student:
            print("Student found:")
            print(student)
        else:
            print("Student not found.")

    def delete_student(self):
        student_id = input("Enter Student ID to delete: ")
        if student_id in self.students:
            del self.students[student_id]
            print("Student deleted.")
        else:
            print("Student not found.")

    def update_student(self):
        student_id = input("Enter Student ID to update: ")
        student = self.students.get(student_id)
        if student:
            print("Leave blank to keep current value.")
            name = input(f"New name (current: {student.name}): ") or student.name
            try:
                age_input = input(f"New age (current: {student.age}): ")
                age = int(age_input) if age_input else student.age
            except ValueError:
                print("Invalid age. Keeping old age.")
                age = student.age
            grade = input(f"New grade (current: {student.grade}): ") or student.grade

            self.students[student_id] = Student(student_id, name, age, grade)
            print("Student updated.")
        else:
            print("Student not found.")


def main():
    manager = StudentManager()

    while True:
        print("\n--- Student Records Manager ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            manager.add_student()
        elif choice == '2':
            manager.view_all_students()
        elif choice == '3':
            manager.search_student()
        elif choice == '4':
            manager.update_student()
        elif choice == '5':
            manager.delete_student()
        elif choice == '6':
            print("Exiting Student Records Manager.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
