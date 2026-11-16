
"""Student Gradebook module."""


class StudentNotFoundError(Exception):
    """Raised when a student does not exist."""
    pass


class Gradebook:

    def __init__(self):
        self.students = {}

    def add_student(self, name, marks):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Invalid student name")

        if isinstance(marks, bool) or not isinstance(marks, (int, float)):
            raise TypeError("Marks must be numeric")

        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100")

        name = name.strip()
        key = name.lower()

        if key in self.students:
            raise ValueError("Student already exists")

        self.students[key] = {
            "name": name,
            "marks": float(marks)
        }

        return self.students[key].copy()

    def get_student(self, name):
        key = name.strip().lower()

        if key not in self.students:
            raise StudentNotFoundError("Student not found")

        return self.students[key].copy()

    def update_marks(self, name, marks):
        key = name.strip().lower()

        if isinstance(marks, bool) or not isinstance(marks, (int, float)):
            raise TypeError("Marks must be numeric")

        if marks < 0 or marks > 100:
            raise ValueError("Invalid marks")

        if key not in self.students:
            raise StudentNotFoundError("Student not found")

        self.students[key]["marks"] = float(marks)

        return self.students[key].copy()

    def remove_student(self, name):
        key = name.strip().lower()

        if key not in self.students:
            raise StudentNotFoundError("Student not found")

        return self.students.pop(key)["name"]

    def list_students(self):
        return sorted(
            [student.copy() for student in self.students.values()],
            key=lambda student: student["name"].lower()
        )

    def average_marks(self):
        if not self.students:
            return 0.0

        total = sum(s["marks"] for s in self.students.values())

        return total / len(self.students)

    def grade_for(self, name):
        marks = self.get_student(name)["marks"]

        if marks >= 90:
            return "A"
        elif marks >= 80:
            return "B"
        elif marks >= 70:
            return "C"
        elif marks >= 60:
            return "D"
        else:
            return "F"

    def count(self):
        return len(self.students)

