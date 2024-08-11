import requests
from src.vacancy_api import VacancyAPI

class HeadHunterAPI(VacancyAPI):
    def get_vacancies(self, query):
        url = 'https://api.hh.ru/vacancies'
        params = {'text': query, 'area': 113}  # 113 - код России
        response = requests.get(url, params=params)
        return response.json()
