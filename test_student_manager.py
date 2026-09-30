import unittest
import tempfile
import os

import student_manager


class TestStudentManager(unittest.TestCase):

    def setUp(self):
        self.test_file = tempfile.NamedTemporaryFile(delete=False)
        self.test_file.close()

        self.original_file = student_manager.DATA_FILE
        student_manager.DATA_FILE = self.test_file.name

    def tearDown(self):
        student_manager.DATA_FILE = self.original_file

        if os.path.exists(self.test_file.name):
            os.remove(self.test_file.name)

    def test_add_student(self):
        students = []

        success, message = student_manager.add_student(
            students,
            "Caleb",
            "CS001",
            "Computer Science"
        )

        self.assertTrue(success)
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0]["name"], "Caleb")

    def test_duplicate_admission_number(self):
        students = [
            {
                "name": "Caleb",
                "admission_no": "CS001",
                "course": "Computer Science"
            }
        ]

        success, message = student_manager.add_student(
            students,
            "John",
            "CS001",
            "Information Technology"
        )

        self.assertFalse(success)
        self.assertEqual(len(students), 1)

    def test_empty_fields(self):
        students = []

        success, message = student_manager.add_student(
            students,
            "",
            "CS002",
            "Computer Science"
        )

        self.assertFalse(success)
        self.assertEqual(len(students), 0)

    def test_search_student(self):
        students = [
            {
                "name": "Caleb",
                "admission_no": "CS001",
                "course": "Computer Science"
            }
        ]

        student = student_manager.search_student(students, "CS001")

        self.assertIsNotNone(student)
        self.assertEqual(student["name"], "Caleb")

    def test_student_not_found(self):
        students = []

        student = student_manager.search_student(students, "CS999")

        self.assertIsNone(student)


if __name__ == "__main__":
    unittest.main()
