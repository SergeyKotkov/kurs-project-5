from abc import ABC, abstractmethod

class VacancyAPI(ABC):
    @abstractmethod
    def get_vacancies(self, query):
        pass