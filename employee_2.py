class Employee:
    def __init__(self, name, day_salary):
        self.name = name
        self.salary = day_salary

    def work(self):
        return 'I come to the office.'

    def __str__(self):
        return f'Посада: {self.name}'

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.daily_salary == other.daily_salary
        return False


class Recruiter(Employee):
    def work(self):
        return "I come to the office and start hiring."

class Developer(Employee):
    def work(self):
        return "I come to the office and start coding."



