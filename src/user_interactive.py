from src.parser import HeadHunterAPI
from src.json_worker import JSONVacancyFileHandler
from src.vacancy import Vacancy

def user_interaction():
    api = HeadHunterAPI()
    file_handler = JSONVacancyFileHandler('vacancies.json')

    while True:
        print("1. Ввести поисковый запрос для запроса вакансий из hh.ru")
        print("2. Получить топ N вакансий по зарплате")
        print("3. Получить вакансии с ключевым словом в описании")
        print("4. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            query = input("Введите поисковый запрос: ")
            vacancies_data = api.get_vacancies(query)
            for item in vacancies_data['items']:
                title = item['name']
                url = item['alternate_url']
                salary = item['salary']['from'] if item['salary'] else None
                description = item['snippet']['requirement']
                vacancy = Vacancy(title, url, salary, description)
                file_handler.add_vacancy(vacancy)

        elif choice == '2':
            n = int(input("Введите количество вакансий: "))
            top_vacancies = file_handler.get_top_n_vacancies_by_salary(n)
            if top_vacancies:
                for vacancy in top_vacancies:
                    print(f"{vacancy.title}: {vacancy.salary}")
            else:
                print("Нет доступных вакансий.")

        elif choice == '3':
            keyword = input("Введите ключевое слово: ")
            vacancies = file_handler.get_vacancies(lambda v: keyword in v.description)
            if vacancies:
                for vacancy in vacancies:
                    print(f"{vacancy.title}: {vacancy.description}")
            else:
                print("Нет вакансий с указанным ключевым словом.")

        elif choice == '4':
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    user_interaction()
