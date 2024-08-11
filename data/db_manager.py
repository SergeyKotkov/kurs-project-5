import psycopg2
from typing import List, Tuple, Optional

class DBManager:
    """
    Класс для взаимодействия с базой данных.
    """

    def __init__(self, dbname: str, user: str, password: str, host: str, port: int):
        """
        Инициализация подключения к базе данных.
        """
        self.conn = psycopg2.connect(
            dbname='kurs5',
            user='postgres',
            password='4779',
            host='losthost',
            port='5432'
        )
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self) -> List[Tuple[str, int]]:
        """
        Получение списка всех компаний и количества вакансий у каждой компании.
        """
        self.cur.execute("""
            SELECT e.name, COUNT(v.id)
            FROM employers e
            LEFT JOIN vacancies v ON e.id = v.employer_id
            GROUP BY e.name
        """)
        return self.cur.fetchall()

    def get_all_vacancies(self) -> List[Tuple[str, str, Optional[int], str]]:
        """
        Получение списка всех вакансий с указанием названия компании, названия вакансии, зарплаты и ссылки на вакансию.
        """
        self.cur.execute("""
            SELECT e.name, v.title, v.salary, v.url
            FROM employers e
            JOIN vacancies v ON e.id = v.employer_id
        """)
        return self.cur.fetchall()

    def get_avg_salary(self) -> Optional[float]:
        """
        Получение средней зарплаты по вакансиям.
        """
        self.cur.execute("""
            SELECT AVG(salary)
            FROM vacancies
            WHERE salary IS NOT NULL
        """)
        result = self.cur.fetchone()
        return result[0] if result else None

    def get_vacancies_with_higher_salary(self) -> List[Tuple[str, str, Optional[int], str]]:
        """
        Получение списка всех вакансий, у которых зарплата выше средней по всем вакансиям.
        """
        avg_salary = self.get_avg_salary()
        if avg_salary is not None:
            self.cur.execute("""
                SELECT e.name, v.title, v.salary, v.url
                FROM employers e
                JOIN vacancies v ON e.id = v.employer_id
                WHERE v.salary > %s
            """, (avg_salary,))
            return self.cur.fetchall()
        return []

    def get_vacancies_with_keyword(self, keyword: str) -> List[Tuple[str, str, Optional[int], str]]:
        """
        Получение списка всех вакансий, в названии которых содержатся переданные в метод слова.
        """
        self.cur.execute("""
            SELECT e.name, v.title, v.salary, v.url
            FROM employers e
            JOIN vacancies v ON e.id = v.employer_id
            WHERE v.title ILIKE %s
        """, (f"%{keyword}%",))
        return self.cur.fetchall()

    def close(self):
        """
        Закрытие подключения к базе данных.
        """
        self.cur.close()
        self.conn.close()
