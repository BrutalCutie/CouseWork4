import json
from abc import ABC, abstractmethod
import requests
import os

from config import DATA_PATH, AREAS_PATH
from src.vacancy import Vacancy


class MainParser(ABC):

    @abstractmethod
    def load_vacancies(self):
        pass


class HHJobs(MainParser):

    def __init__(self, city: str = "", search_field: str = "", salary: str = '', top: int = 0):
        self.url = 'https://api.hh.ru/vacancies'
        self.vacancies = []
        self.params = {'text': '', 'page': 0, 'per_page': 100}

        self.city = city
        self.search_field = search_field
        self.salary = salary
        self.top_vac = top
        self.salary_lower = 0
        self.salary_upper = 0
        self.salary_range = False

        if self.salary.isdigit():
            self.params['salary'] = salary

        if self.search_field != "":
            self.params['text'] = search_field

        if self.city != "":
            city_id = self.get_area_id(city)
            self.params['area'] = city_id

        if '-' in self.salary:
            self.salary_lower, self.salary_upper = list(map(int, salary.split(" - ")))
            self.salary_range = True

            self.params['salary'] = self.salary_lower

    def load_vacancies(self):
        while True:

            response = requests.get(self.url, params=self.params)
            response_data: dict = response.json()

            if response_data.get("items"):
                self.vacancies.extend(response_data['items'])

            if not response_data.get('pages') or self.params['page'] == response_data['pages']:
                break
            else:
                self.params['page'] += 1



    @staticmethod
    def get_area_id(city: str) -> int | None:

        with open(AREAS_PATH, 'r', encoding='utf8') as areas_file_data:
            areas = json.load(areas_file_data)[0]['areas']

        for area_data in areas:
            for cities in area_data['areas']:
                if city.lower() == cities['name'].lower():
                    return cities['id']
        else:
            return None

if __name__ == '__main__':

    getter = HHJobs()
