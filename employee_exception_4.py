from datetime import datetime


class EmailAlreadyExistsException(Exception):
    pass


class Employee:
    def __init__(self, name, daily_salary, email):
        self.name = name
        self.daily_salary = daily_salary
        self.email = email
        self.save_email()

    def work(self):
        return "I come to the office."

    def check_salary(self, days):
        work_days = 0
        current_day = 0

        while current_day < days:
            if current_day % 7 < 5:  # Перевірка, що це робочий день (не вихідний)
                work_days += 1
            current_day += 1

        return work_days * self.daily_salary

    def save_email(self):
        try:
            with open("emails.csv", "a") as file:
                file.write(f"{self.email}\n")
        except Exception as e:
            self.log_error(e)

    def validate(self):
        try:
            with open("emails.csv", "r") as file:
                emails = file.read().splitlines()
                if self.email in emails:
                    raise EmailAlreadyExistsException(f"Email '{self.email}' already exists.")
        except FileNotFoundError:
            pass  # Якщо файл не існує, перевірка на наявність не потрібна
        except Exception as e:
            self.log_error(e)

    def log_error(self, exception):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("logs.txt", "a") as file:
            file.write(f"{timestamp} | {str(exception)}\n")

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
    def __init__(self, name, daily_salary, tech_stack, email):
        super().__init__(name, daily_salary, email)
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
            email = f"{self.email}-{other.email}"
            return Developer(name, daily_salary, tech_stack, email)
        else:
            raise TypeError("Invalid type for addition.")



