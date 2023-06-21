import csv
import requests

class Candidate:
    def __init__(self, first_name, last_name, email, tech_stack, main_skill, main_skill_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def generate_candidates(cls, path_or_url):
        if path_or_url.startswith("http"):
            response = requests.get(path_or_url)
            content = response.content.decode("utf-8")
            reader = csv.reader(content.splitlines(), delimiter=",")
        else:
            with open(path_or_url, "r") as file:
                reader = csv.reader(file, delimiter=",")

        candidates = []

        next(reader)  # Пропустити заголовок

        for row in reader:
            full_name, email, tech_stack, main_skill, main_skill_grade = row
            first_name, last_name = full_name.split()
            tech_stack = tech_stack.split("|")
            candidate = Candidate(first_name, last_name, email, tech_stack, main_skill, main_skill_grade)
            candidates.append(candidate)

        return candidates


# Приклад використання
url = "https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv"
candidates = Candidate.generate_candidates(url)

for candidate in candidates:
    print(f"Full Name: {candidate.full_name}")
    print(f"Email: {candidate.email}")
    print(f"Technologies: {', '.join(candidate.tech_stack)}")
    print(f"Main Skill: {candidate.main_skill}")
    print(f"Main Skill Grade: {candidate.main_skill_grade}")
    print()
