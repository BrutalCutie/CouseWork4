import json
import requests

from src.vacancies_getter import HHJobs


def main():
    search_field = input("Введите поисковой запрос: ")
    top_n = input("Введите количество выводимых вакансий: ")
    city_search = input("Введите город/село/деревню для поиска вакансий (оставьте пустым, чтобы искать по всем): ")
    salary_range = input("Введите диапазон зарплаты (Nmin - Nmax): ")
    keywords = input("Введите ключевые слова для поиска (разделение через \", \"): ")

    if keywords != '':
        keywords = keywords.split(', ')

    if ' - ' in salary_range:
        salary_range = salary_range.split(' - ')

    vacancies = HHJobs().get_filtered_vacancies(keywords=keywords,
                                                salary_range=salary_range,
                                                search_field=search_field,
                                                city=city_search,
                                                top_n=top_n)

    return vacancies


if __name__ == '__main__':
    print(main())
