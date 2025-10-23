"""Student grading system."""

class Student
    """Represents a student with grades and status."""

    def __init__(self, student_id: str, name: str):
        """Initialize student with ID and name."""
        if not student_id or not name:
            raise ValueError("Student ID and name cannot be empty.")

        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor = False
        self.letter = None

    def add_grade(self, grade: float):
        """Add a numeric grade between 0 and 100."""
        if not isinstance(grade, (int, float)):
            print(f"Invalid grade '{grade}': must be a number.")
            return
        if not 0 <= grade <= 100:
            print(f"Invalid grade '{grade}': must be between 0 and 100.")
            return
        self.grades.append(grade)

    def calculate_average(self):
        """Calculate and return the average grade."""
        if not self.grades:
            print("No grades available.")
            return 0.0
        return sum(self.grades) / len(self.grades)

    def determine_letter_grade(self):
        """Determine letter grade and pass/fail status."""
        avg = float(self.calculate_average())
        if avg >= 90:
            self.letter = "A"
        elif avg >= 80:
            self.letter = "B"
        elif avg >= 70:
            self.letter = "C"
        elif avg >= 60:
            self.letter = "D"
        else:
            self.letter = "F"

        self.is_passed = avg >= 60
        return self.letter

    def check_honor(self):
        """Check if student is honor student (average >= 90)."""
        avg = self.calculate_average()
        self.honor = avg >= 90

    def delete_grade(self, index: int):
        """Delete a grade by index, safely."""
        if 0 <= index < len(self.grades):
            del self.grades[index]
        else:
            print(f"Invalid index {index}. No grade deleted.")

    def remove_grade_by_value(self, value: float) -> bool:
        """Remove the first occurrence of a grade by value. Returns True if removed."""
        # comparación tolerante para floats
        try:
            # buscar primera coincidencia con tolerancia
            for i, g in enumerate(self.grades):
                if isinstance(g, (int, float)) and abs(g - value) < 1e-9:
                    removed = self.grades.pop(i)
                    print(f"Nota {removed} eliminada correctamente.")
                    return True
            print(f"No se encontró la nota {value}. No se eliminó.")
            return False
        except Exception as e:
            print(f"Error al eliminar por valor: {e}")
            return False

    def remove_grade_by_index(self, index: int) -> bool:
        """Remove a grade by index (0-based). Returns True if removed."""
        if 0 <= index < len(self.grades):
            removed = self.grades.pop(index)
            print(f"Nota en índice {index} ({removed}) eliminada correctamente.")
            return True
        else:
            print(f"Índice {index} fuera de rango. No se eliminó.")
            return False

    def report(self):
        """Display student's summary."""
        self.determine_letter_grade()
        self.check_honor()
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Grades: {self.grades}")
        print(f"Average: {self.calculate_average():.2f}")
        print(f"Letter Grade: {self.letter}")
        print(f"Passed: {'Yes' if self.is_passed else 'No'}")
        print(f"Honor Student: {'Yes' if self.honor else 'No'}")

    def summary(self) -> str:
        """Generate a formatted summary report for the student."""
        self.determine_letter_grade()
        self.check_honor()
        num = len(self.grades)
        avg = self.calculate_average()
        return (
            f"Student ID: {self.student_id}\n"
            f"Student Name: {self.name}\n"
            f"Number of Grades: {num}\n"
            f"Average Grade: {avg:.2f}\n"
            f"Letter Grade: {self.letter}\n"
            f"Pass/Fail: {'Pass' if self.is_passed else 'Fail'}\n"
            f"Honor Roll: {'Yes' if self.honor else 'No'}"
        )


def start_run():
    """Run sample test."""
    student1 = Student("123", "Alice")
    student1.add_grade(95)
    student1.add_grade(72.5)
    student1.add_grade("Fifty")  # Invalid input handled
    student1.delete_grade(5)  # Invalid index handled
    student1.report()


if __name__ == "__main__":
    start_run()