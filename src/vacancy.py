class Vacancy:
    def __init__(self, title, url, salary, description):
        self.title = title
        self.url = url
        self.salary = self.validate_salary(salary)
        self.description = description

    def validate_salary(self, salary):
        if salary:
            return salary
        else:
            return "Зарплата не указана"

    def get_salary_for_sorting(self):
        if self.salary == "Зарплата не указана":
            return 0
        return self.salary

    def __lt__(self, other):
        return self.get_salary_for_sorting() < other.get_salary_for_sorting()
