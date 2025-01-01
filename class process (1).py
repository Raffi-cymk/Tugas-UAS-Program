class StudentProcess:
    def _init_(self, data, view):
        self.data = data
        self.view = view

    def add_student(self):
        try:
            name = input("Enter student name: ").strip()
            if not name:
                raise ValueError("Name cannot be empty.")
            score = input("Enter student score (0-100): ").strip()
            if not score.isdigit() or not (0 <= int(score) <= 100):
                raise ValueError("Score must be an integer between 0 and 100.")
            self.data.add_student(name, int(score))
            self.view.display_message("Student added successfully!")
        except ValueError as e:
            self.view.display_message(f"Error: {e}")

    def show_students(self):
        if not self.data.students:
            self.view.display_message("No students in the list.")
        else:
            self.view.display_table(self.data.students)