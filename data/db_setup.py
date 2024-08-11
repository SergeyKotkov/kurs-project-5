import psycopg2
from typing import Dict, List, Tuple

def create_tables(db_params: Dict[str, str]) -> None:
    """
    Создание таблиц в базе данных.
    """
    commands = (
        """
        CREATE TABLE IF NOT EXISTS employers (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            description TEXT,
            url VARCHAR(255)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS vacancies (
            id SERIAL PRIMARY KEY,
            employer_id INT REFERENCES employers(id),
            title VARCHAR(255),
            salary INT,
            url VARCHAR(255)
        )
        """
    )
    conn = psycopg2.connect(
        dbname=db_params['dbname'],
        user=db_params['user'],
        password=db_params['password'],
        host=db_params['host'],
        port=db_params['port']
    )
    cur = conn.cursor()
    for command in commands:
        cur.execute(command)
    conn.commit()
    cur.close()
    conn.close()

def insert_employers(employers: List[Dict[str, str]], db_params: Dict[str, str]) -> List[int]:
    """
    Вставка данных о работодателях в базу данных и возврат их идентификаторов.
    """
    conn = psycopg2.connect(
        dbname=db_params['dbname'],
        user=db_params['user'],
        password=db_params['password'],
        host=db_params['host'],
        port=db_params['port']
    )
    cur = conn.cursor()
    employer_ids = []
    for employer in employers:
        name = employer.get('name', 'Unknown')
        description = employer.get('description', 'No description')
        url = employer.get('url', 'No URL')
        cur.execute(
            "INSERT INTO employers (name, description, url) VALUES (%s, %s, %s) RETURNING id",
            (name, description, url)
        )
        employer_id = cur.fetchone()[0]
        employer_ids.append(employer_id)
    conn.commit()
    cur.close()
    conn.close()
    return employer_ids

def insert_vacancies(vacancies: List[Dict[str, str]], employer_id: int, db_params: Dict[str, str]) -> None:
    """
    Вставка данных о вакансиях в базу данных.
    """
    conn = psycopg2.connect(
        dbname=db_params['dbname'],
        user=db_params['user'],
        password=db_params['password'],
        host=db_params['host'],
        port=db_params['port']
    )
    cur = conn.cursor()
    for vacancy in vacancies:
        title = vacancy.get('name', 'Unknown')
        salary = None
        if vacancy.get('salary') is not None:
            salary = vacancy['salary'].get('from', None)
        url = vacancy.get('alternate_url', 'No URL')
        cur.execute(
            "INSERT INTO vacancies (employer_id, title, salary, url) VALUES (%s, %s, %s, %s)",
            (employer_id, title, salary, url)
        )
    conn.commit()
    cur.close()
    conn.close()
