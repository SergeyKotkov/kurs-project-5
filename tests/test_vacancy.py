import unittest
from src.vacancy import Vacancy

class TestVacancy(unittest.TestCase):
    def test_validate_salary(self):
        vacancy = Vacancy("Test", "http://test.com", None, "Description")
        self.assertEqual(vacancy.salary, "Зарплата не указана")

    def test_compare_vacancies(self):
        vacancy1 = Vacancy("Test1", "http://test1.com", 50000, "Description1")
        vacancy2 = Vacancy("Test2", "http://test2.com", 60000, "Description2")
        self.assertTrue(vacancy1 < vacancy2)

if __name__ == "__main__":
    unittest.main()
