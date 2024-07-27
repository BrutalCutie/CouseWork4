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
    """
    Класс для парсинга вакансий по API с сайта www.hh.ru
    """

    def __init__(self, city: str = "", search_field: str = "", top: int = 0):
        """
        Класс для поиска вакансий по запросу пользователя

        :param city: Город поиска. По умолчанию пуст. Это означает, что поиск будет производиться по всем городам.
        :param search_field: Поле для поиска.
        :param top: Вывод определённого количества вакансий. По умолчанию производится вывод всех вакансий.
        """

        self.url = "https://api.hh.ru/vacancies"
        self.vacancies: list = []
        self.primary_vacancies: list = []
        self.params = {"page": 0, "per_page": 100, "only_with_salary": True}
        self.city = city
        self.top_vac = top
        self.total_vacs = 0

        if search_field != "":
            self.params["text"] = search_field

        if self.city != "":
            city_id = self.get_area_id(city)
            self.params["area"] = city_id

        self.load_vacancies()

    def load_vacancies(self) -> list[dict]:
        """
        Функция производит загрузку всех вакансий, соответвующих данным при инициализации
        :return: список словарей с вакансиями
        """
        while True:

            response = requests.get(self.url, params=self.params)
            response_data: dict = response.json()

            if response_data.get("items"):
                self.vacancies.extend(response_data["items"])

            if not response_data.get("pages") or self.params["page"] == response_data["pages"]:
                break
            else:
                self.total_vacs += len(response_data["items"])
                self.params["page"] += 1

        self.primary_vacancies = self.vacancies.copy()

        return self.vacancies

    def reset_to_primary(self) -> None:
        """
        Содержание списка может быть измененр в ходе фильтраций
        по зарплате, ключевым словам и часть вакансий может быть потеряна.
        Эта функция сбрасывает вакансии к изначальному виду.
        :return:
        """

        self.vacancies = self.primary_vacancies
        self.total_vacs = len(self.vacancies)

    def filter_by_salary(self, salary: str):
        """
        Функция производит фильтрацию по списку вакансий по зарплате. Можно указать диапазон или же одиночное число.
        В случае если будет указано одиночное число - будут отсечены результаты с зарплатой ниже указанной
        :param salary: желаемая минимальная зарплата или диапозон зарплаты через "-"
        :return:
        """

        salary_lower = None
        salary_upper = None
        salary_range = False

        if "-" in salary:
            salary_lower, salary_upper = list(map(int, salary.split("-")))
            salary_range = True

        self.vacancies = sorted(self.vacancies, key=lambda _: _["salary"]["from"] or _["salary"]["to"], reverse=True)

        filtered_data = []

        for vacancy in self.vacancies:
            salary_target = vacancy["salary"]["from"] or vacancy["salary"]["to"]
            if salary_range:
                if salary_lower <= salary_target <= salary_upper:
                    filtered_data.append(vacancy)
                    continue

            if salary_target >= int(salary):
                filtered_data.append(vacancy)

        self.vacancies = filtered_data
        self.total_vacs = len(self.vacancies)

        return self

    def filter_by_keywords(self, keywords: str):
        """
        Функция фильтрует по ключевым словам в списке вакансий и отсекает вакансии где нет совпадений
        :param keywords: Ключевые слова. Слова разделяются через пробел.
        :return:
        """
        filtered_data = []

        keywords = [x.lower() for x in keywords.split(" ")]

        for vacancy in self.vacancies:
            vac_desrc = vacancy.get("snippet", {}).get("responsibility")

            if not vac_desrc:
                continue

            for kw in keywords:

                if kw in vac_desrc:
                    filtered_data.append(vacancy)
                    break

        self.vacancies = filtered_data
        self.total_vacs = len(self.vacancies)

        return self

    def as_vacancy_class(self) -> list[Vacancy]:
        """
        Функция возвращает список с экземплярами класса вакансий(Vacancy).
        :return:
        """
        vac_classes_list = []
        top_stop = self.top_vac != 0

        for index, vac in enumerate(self.vacancies, 1):
            vac_classes_list.append(Vacancy(vacancy_data=vac))

            if top_stop and index == self.top_vac:
                break

        return vac_classes_list

    def get_raw_data(self) -> list[dict]:
        """
        Функция возвращает сырые данные списка вакансий
        :return:
        """
        if self.top_vac != 0 and len(self.vacancies) >= self.top_vac:
            return self.vacancies[: self.top_vac]

        return self.vacancies

    @staticmethod
    def get_area_id(city: str) -> int | None:
        """
        Функция трансформирует город в id города, для работы для поиска вакансий по городу.
        :param city: Город
        :return:
        """

        with open(AREAS_PATH, "r", encoding="utf8") as areas_file_data:
            areas = json.load(areas_file_data)[0]["areas"]

        for area_data in areas:
            for cities in area_data["areas"]:
                if city.lower() == cities["name"].lower():
                    return cities["id"]
        else:
            raise ValueError("Город не найден")


if __name__ == "__main__":
    all_vacs = HHJobs("уфа", "python", 5)

    filtered_salary = all_vacs.filter_by_salary("50000")
