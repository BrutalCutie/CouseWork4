import json
import requests

from src.vacancies_getter import HHJobs


def main():
    while True:
        search_field = input("Введите поисковой запрос: ")

        if search_field != '':
            break

        print('\nПОИСКОВЫЙ ЗАПРОС НЕ МОЖЕТ БЫТЬ ПУСТЫМ !\n')

    top_n = input("Введите количество выводимых вакансий (оставьте пустым, чтобы вывести все): ")
    city_search = input("Введите город/село/деревню для поиска вакансий (оставьте пустым, чтобы искать по всем): ")
    salary_range = input("Введите минимальную зарлату или диапазон зарплаты (Nmin-Nmax): ")
    keywords = input("Введите ключевые слова для поиска (разделение слов через пробел): ")

    # vacancies = HHJobs(city=city_search, search_field=search_field, top=0)
    params = {
        'city': city_search,
        'search_field': search_field,
        'top': top_n
    }

    vacancies = HHJobs(**params)

    if keywords != '':
        pass

    if '-' in salary_range:
        pass

    return vacancies
