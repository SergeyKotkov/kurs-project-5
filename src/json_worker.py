import json
from src.vacancy_file_handler import VacancyFileHandler
from src.vacancy import Vacancy

class JSONVacancyFileHandler(VacancyFileHandler):
    def __init__(self, file_path):
        self.file_path = file_path

    def add_vacancy(self, vacancy):
        vacancies = self.load_vacancies()
        vacancies.append(vacancy.__dict__)
        self.save_vacancies(vacancies)

    def get_vacancies(self, criteria):
        vacancies = self.load_vacancies()
        return [Vacancy(**v) for v in vacancies if criteria(Vacancy(**v))]

    def delete_vacancy(self, criteria):
        vacancies = self.load_vacancies()
        vacancies = [v for v in vacancies if not criteria(Vacancy(**v))]
        self.save_vacancies(vacancies)

    def load_vacancies(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_vacancies(self, vacancies):
        with open(self.file_path, 'w') as file:
            json.dump(vacancies, file, default=lambda x: x.__dict__)

    def get_top_n_vacancies_by_salary(self, n):
        vacancies = self.get_vacancies(lambda v: True)
        vacancies.sort(reverse=True)
        return vacancies[:n]

