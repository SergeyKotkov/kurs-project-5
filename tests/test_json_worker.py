import unittest
from src.json_worker import JSONVacancyFileHandler
from src.vacancy import Vacancy

class TestJSONVacancyFileHandler(unittest.TestCase):
    def setUp(self):
        self.file_handler = JSONVacancyFileHandler('test_vacancies.json')

    def tearDown(self):
        import os
        os.remove('test_vacancies.json')

    def test_add_and_get_vacancy(self):
        vacancy = Vacancy("Test", "http://test.com", 50000, "Description")
        self.file_handler.add_vacancy(vacancy)
        vacancies = self.file_handler.get_vacancies(lambda v: True)
        self.assertEqual(len(vacancies), 1)
        self.assertEqual(vacancies[0].title, "Test")

if __name__ == "__main__":
    unittest.main()
