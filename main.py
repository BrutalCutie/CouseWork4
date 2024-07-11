import json
import requests

from src.vacancies_getter import HHJobs


def main():

    search_field = input("Введите поисковой запрос: ")
    top_n = input("Введите количество выводимых вакансий: ")
    city_search = input("Введите город для поиска вакансий (оставьте пустым, чтобы искать по всем): ")
    salary_range = input("Введите диапазон зарплаты (Nmin - Nmax): ")
    keywords = input("Введите ключевые слова для поиска (разделение через \", \"): ")




