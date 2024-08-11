from data.db_setup import create_tables, insert_employers, insert_vacancies
from data.data_fetcher import get_employers, get_vacancies
from data.db_manager import DBManager
from typing import Dict

# Параметры подключения к базе данных
DB_PARAMS: Dict[str, str] = {
    'dbname': 'kurs5',
    'user': 'postgres',
    'password': '4779',
    'host': 'localhost',
    'port': 5432
}

# ID компаний
employer_ids = [1740, 3529, 2180, 80, 39305, 15478, 1373, 4934, 2344, 9498]

# Создание таблиц
create_tables(DB_PARAMS)

# Получение данных о работодателях и вакансиях
employers = get_employers(employer_ids)
for employer in employers:
    vacancies = get_vacancies(employer['id'])
    insert_employers([employer], DB_PARAMS)
    insert_vacancies(vacancies, employer['id'], DB_PARAMS)

def user_interaction():
    """
    Функция взаимодействия с пользователем.
    """
    db_manager = DBManager(**DB_PARAMS)

    print("Companies and vacancies count:")
    for company, count in db_manager.get_companies_and_vacancies_count():
        print(f"{company}: {count} vacancies")

    print("\nAll vacancies:")
    for company, title, salary, url in db_manager.get_all_vacancies():
        print(f"{company}: {title} - Salary: {salary} - URL: {url}")

    print("\nAverage salary:")
    avg_salary = db_manager.get_avg_salary()
    print(f"Average salary: {avg_salary}")

    print("\nVacancies with higher salary:")
    for company, title, salary, url in db_manager.get_vacancies_with_higher_salary():
        print(f"{company}: {title} - Salary: {salary} - URL: {url}")

    print("\nVacancies with keyword 'python':")
    for company, title, salary, url in db_manager.get_vacancies_with_keyword("python"):
        print(f"{company}: {title} - Salary: {salary} - URL: {url}")

    db_manager.close()

if __name__ == "__main__":
    user_interaction()


# Использование DBManager
db_manager = DBManager(**DB_PARAMS)
print("Companies and vacancies count:")
print(db_manager.get_companies_and_vacancies_count())
print("\nAll vacancies:")
print(db_manager.get_all_vacancies())
print("\nAverage salary:")
print(db_manager.get_avg_salary())
print("\nVacancies with higher salary:")
print(db_manager.get_vacancies_with_higher_salary())
print("\nVacancies with keyword 'python':")
print(db_manager.get_vacancies_with_keyword("python"))
db_manager.close()

