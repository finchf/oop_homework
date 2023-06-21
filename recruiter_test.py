import unittest
from employee_exception_4 import Recruiter

class RecruiterTestCase(unittest.TestCase):
    def setUp(self):
        self.recruiter = Recruiter("John Doe", 100, "HR")

    def test_work(self):
        self.assertEqual(self.recruiter.work(), "I come to the office and start hiring.")

    def test_check_salary(self):
        self.assertEqual(self.recruiter.check_salary(10), 500)

    def test_str(self):
        self.assertEqual(str(self.recruiter), "Recruiter: John Doe")

    def test_eq(self):
        other_recruiter = Recruiter("Jane Smith", 100, "HR")
        self.assertTrue(self.recruiter == other_recruiter)

if __name__ == '__main__':
    unittest.main()
