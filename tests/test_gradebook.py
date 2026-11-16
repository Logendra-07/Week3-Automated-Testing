
import unittest

from student_gradebook import Gradebook, StudentNotFoundError


class TestGradebook(unittest.TestCase):

    def setUp(self):
        self.book = Gradebook()

    # Test 1: Add student
    def test_add_student(self):
        result = self.book.add_student("Arun", 85)
        self.assertEqual(result["name"], "Arun")
        self.assertEqual(result["marks"], 85.0)

    # Test 2: Retrieve student
    def test_get_student(self):
        self.book.add_student("Arun", 85)
        result = self.book.get_student("Arun")
        self.assertEqual(result["marks"], 85.0)

    # Test 3: Case insensitive search
    def test_case_insensitive_search(self):
        self.book.add_student("Arun", 85)
        self.assertEqual(self.book.get_student("ARUN")["marks"], 85.0)

    # Test 4: Duplicate student
    def test_duplicate_student(self):
        self.book.add_student("Arun", 85)
        with self.assertRaises(ValueError):
            self.book.add_student("Arun", 90)

    # Test 5: Empty name
    def test_empty_name(self):
        with self.assertRaises(ValueError):
            self.book.add_student("", 80)

    # Test 6: Non-numeric marks
    def test_invalid_marks_type(self):
        with self.assertRaises(TypeError):
            self.book.add_student("Arun", "eighty")

    # Test 7: Negative marks
    def test_negative_marks(self):
        with self.assertRaises(ValueError):
            self.book.add_student("Arun", -10)

    # Test 8: Marks above 100
    def test_marks_above_100(self):
        with self.assertRaises(ValueError):
            self.book.add_student("Arun", 110)

    # Test 9: Zero marks
    def test_zero_marks(self):
        self.book.add_student("Arun", 0)
        self.assertEqual(self.book.get_student("Arun")["marks"], 0.0)

    # Test 10: Maximum marks
    def test_maximum_marks(self):
        self.book.add_student("Arun", 100)
        self.assertEqual(self.book.get_student("Arun")["marks"], 100.0)

    # Test 11: Update marks
    def test_update_marks(self):
        self.book.add_student("Arun", 70)
        self.book.update_marks("Arun", 95)
        self.assertEqual(self.book.get_student("Arun")["marks"], 95.0)

    # Test 12: Update missing student
    def test_update_missing_student(self):
        with self.assertRaises(StudentNotFoundError):
            self.book.update_marks("Unknown", 80)

    # Test 13: Remove student
    def test_remove_student(self):
        self.book.add_student("Arun", 85)
        self.book.remove_student("Arun")
        self.assertEqual(self.book.count(), 0)

    # Test 14: Get missing student
    def test_missing_student(self):
        with self.assertRaises(StudentNotFoundError):
            self.book.get_student("Unknown")

    # Test 15: Calculate average
    def test_average_marks(self):
        self.book.add_student("Arun", 80)
        self.book.add_student("Bala", 100)
        self.assertEqual(self.book.average_marks(), 90.0)

    # Test 16: Grade calculation
    def test_grade_calculation(self):
        self.book.add_student("Arun", 95)
        self.assertEqual(self.book.grade_for("Arun"), "A")

    # Test 17: Integration test
    def test_student_lifecycle(self):
        self.book.add_student("Arun", 70)
        self.book.update_marks("Arun", 90)

        self.assertEqual(self.book.grade_for("Arun"), "A")
        self.assertEqual(self.book.average_marks(), 90.0)

        self.book.remove_student("Arun")
        self.assertEqual(self.book.count(), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
