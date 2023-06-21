import unittest
from employee_exception_4 import Employee

class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("John Doe", 100)

    def test_work(self):
        self.assertEqual(self.employee.work(), "I come to the office.")

    def test_check_salary(self):
        self.assertEqual(self.employee.check_salary(10), 500)

    def test_str(self):
        self.assertEqual(str(self.employee), "Посада: John Doe")

    def test_eq(self):
        other_employee = Employee("Jane Smith", 100)
        self.assertTrue(self.employee == other_employee)

if __name__ == '__main__':
    unittest.main()
