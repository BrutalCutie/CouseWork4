import json
from abc import ABC, abstractmethod
import requests

from config import AREAS_PATH
from src.vacancy import Vacancy


class MainParser(ABC):

    @abstractmethod
    def load_vacancies(self):
        pass


class HHJobs(MainParser):

    def __init__(self, city: str = "", search_field: str = "", salary: str = '', top: int = 0):
        self.url = 'https://api.hh.ru/vacancies'
        self.vacancies = []
        self.params = {'text': '', 'page': 0, 'per_page': 100, "only_with_salary": True}

        self.city = city
        self.search_field = search_field
        self.salary = salary
        self.top_vac = top
        self.salary_lower = 0
        self.salary_upper = 0
        self.salary_range = False
        self.total_vacs = 0

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

    def load_vacancies(self) -> None:
        while True:

            response = requests.get(self.url, params=self.params)
            response_data: dict = response.json()

            if response_data.get("items"):
                self.vacancies.extend(response_data['items'])

            if not response_data.get('pages') or self.params['page'] == response_data['pages']:
                break
            else:
                self.total_vacs += len(response_data['items'])
                self.params['page'] += 1

        self.filter_by_salary()

    def filter_by_salary(self) -> None:

        self.vacancies = sorted(self.vacancies, key=lambda _: _['salary']['from'] or _['salary']['to'], reverse=True)

        if self.salary_range:
            tmp = []

            for vacancy in self.vacancies:

                salary_target = vacancy['salary']['from'] or vacancy['salary']['to']
                if self.salary_lower < salary_target < self.salary_upper:
                    tmp.append(vacancy)
            self.vacancies = tmp

    def as_vacancy_class(self) -> list[Vacancy]:
        vac_classes_list = []
        top_stop = self.top_vac != 0

        for index, vac in enumerate(self.vacancies, 1):
            vac_classes_list.append(Vacancy(vacancy_data=vac))

            if top_stop and index == self.top_vac:
                break

        return vac_classes_list

    def get_raw_data(self) -> list[dict]: return self.vacancies

    @staticmethod
    def get_area_id(city: str) -> int | None:

        with open(AREAS_PATH, 'r', encoding='utf8') as areas_file_data:
            areas = json.load(areas_file_data)[0]['areas']

        for area_data in areas:
            for cities in area_data['areas']:
                if city.lower() == cities['name'].lower():
                    return cities['id']
        else:
            raise ValueError("Город не найден")


if __name__ == '__main__':

    getter = HHJobs('уфа', "120000")
    getter.load_vacancies()

    # print(getter)
    for i in getter.as_vacancy_class():
        print(i)
    print(f"Всего найдено {getter.total_vacs} Вакансий")
