from datetime import datetime, timedelta


class Employee:
    def __init__(self, name, daily_salary):
        self.name = name
        self.daily_salary = daily_salary

    def work(self):
        return "I come to the office."

    def check_salary(self, days):
        start_date = datetime.now() - timedelta(days=days)
        work_days = 0

        current_date = datetime.now()
        while current_date >= start_date:
            if current_date.weekday() < 5:  # Перевірка, що це робочий день (не вихідний)
                work_days += 1
            current_date -= timedelta(days=1)

        return work_days * self.daily_salary

    def __str__(self):
        return f"Посада: {self.name}"

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.daily_salary == other.daily_salary
        return False


class Recruiter(Employee):
    def work(self):
        return "I come to the office and start hiring."


class Developer(Employee):
    def __init__(self, name, daily_salary, tech_stack):
        super().__init__(name, daily_salary)
        self.tech_stack = tech_stack

    def work(self):
        return "I come to the office and start coding."

    def __eq__(self, other):
        if isinstance(other, Developer):
            return len(self.tech_stack) == len(other.tech_stack)
        return False

    def __add__(self, other):
        if isinstance(other, Developer):
            name = f"{self.name} {other.name}"
            tech_stack = list(set(self.tech_stack + other.tech_stack))  # Об'єднання унікальних технологій
            daily_salary = max(self.daily_salary, other.daily_salary)  # Більша зарплата
            return Developer(name, daily_salary, tech_stack)
        else:
            raise TypeError("Invalid type for addition.")


recruiter = Recruiter("Рекрутер", 100)
developer1 = Developer("Розробник 1", 200, ["Python", "JavaScript"])
developer2 = Developer("Розробник 2", 250, ["Java", "JavaScript"])

print(recruiter.work())  #  "I come to the office and start hiring."
print(developer1.work())  #  "I come to the office and start coding."

print(recruiter.check_salary(10))  # Розрахунок ЗП рекрутера за 10 останніх робочих днів
print(developer1.check_salary(20))  # Розрахунок ЗП розробника 1 за 20 останніх робочих днів

print(recruiter)  #  "Посада: Рекрутер"
print(developer1)  #  "Посада: Розробник 1"

print(developer1 == developer2)  #  False
print(developer1 == Developer("Інший розробник", 200, ["Python", "JavaScript"]))  #  True


