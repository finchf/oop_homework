import unittest
from employee_exception_4 import Developer

class DeveloperTestCase(unittest.TestCase):
    def setUp(self):
        self.developer = Developer("John Doe", 100, "Python")

    def test_work(self):
        self.assertEqual(self.developer.work(), "I come to the office and start coding.")

    def test_check_salary(self):
        self.assertEqual(self.developer.check_salary(10), 1000)

    def test_str(self):
        self.assertEqual(str(self.developer), "Developer: John Doe")

    def test_eq(self):
        other_developer = Developer("Jane Smith", 100, "Python")
        self.assertTrue(self.developer == other_developer)

if __name__ == '__main__':
    unittest.main()
