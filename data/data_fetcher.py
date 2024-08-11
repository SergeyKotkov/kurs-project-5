import requests
from typing import List, Dict

def get_employers(employer_ids: List[int]) -> List[Dict[str, str]]:
    """
    Получение данных о работодателях с API hh.ru.
    """
    employers = []
    for employer_id in employer_ids:
        url = f"https://api.hh.ru/employers/{employer_id}"
        response = requests.get(url)
        if response.status_code == 200:
            employer_data = response.json()
            employers.append(employer_data)
            print(f"Employer data for ID {employer_id}: {employer_data}")  # Отладочный вывод
    return employers

def get_vacancies(employer_id: int) -> List[Dict[str, str]]:
    """
    Получение данных о вакансиях с API hh.ru.
    """
    url = f"https://api.hh.ru/vacancies?employer_id={employer_id}"
    response = requests.get(url)
    if response.status_code == 200:
        vacancies_data = response.json()['items']
        print(f"Vacancies data for employer ID {employer_id}: {vacancies_data}")  # Отладочный вывод
        return vacancies_data
    return []
