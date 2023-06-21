import unittest
from decorators_5 import Candidate

class CandidateTestCase(unittest.TestCase):
    def setUp(self):
        self.candidate = Candidate("John", "Doe", "johndoe@example.com", ["Python", "Django"], "Python", "Senior")

    def test_full_name(self):
        self.assertEqual(self.candidate.full_name, "John Doe")

    def test_str(self):
        self.assertEqual(str(self.candidate), "Candidate: John Doe")

    def test_eq(self):
        other_candidate = Candidate("Jane", "Smith", "janesmith@example.com", ["Python", "Django"], "Python", "Senior")
        self.assertTrue(self.candidate == other_candidate)

if __name__ == '__main__':
    unittest.main()
