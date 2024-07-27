from src.vacancies_getter import HHJobs
from src.file_saver import JsonSaver


def main() -> None:
    """
    Главная функция, демонстрирующая работу программы через консоль
    :return:
    """

    while True:
        search_field = input("Введите поисковой запрос: ")

        if search_field != "":
            break

        print("\nПОИСКОВЫЙ ЗАПРОС НЕ МОЖЕТ БЫТЬ ПУСТЫМ !\n")

    top_n = input("Введите количество выводимых вакансий (оставьте пустым, чтобы вывести все): ")
    city_search = input("Введите город/село/деревню для поиска вакансий (оставьте пустым, чтобы искать по всем): ")
    salary = input("Введите минимальную зарлату или диапазон зарплаты (Nmin-Nmax): ")
    keywords = input("Введите ключевые слова для поиска (разделение слов через пробел. Можно оставить пустым): ")

    params = {"city": city_search, "search_field": search_field, "top": int(top_n) if top_n != "" else 0}

    print("\rИдёт поиск вакансий", end="")
    vacancies = HHJobs(**params)

    if keywords != "":
        vacancies = vacancies.filter_by_keywords(keywords.lower())

    if salary != "":
        vacancies = vacancies.filter_by_salary(salary)

    print("Вот вакансии по вашему запросу:\n")

    for vac in vacancies.as_vacancy_class():
        print(vac)
    print(f"Всего найдено вакансий: {vacancies.total_vacs}\n")

    is_need_save = False
    if vacancies.total_vacs > 0:
        is_need_save = input("Желаете сохранить результаты. Да/Нет[Нет]: ").lower() == "да"

    if is_need_save:
        file_name = input("Напишите название файла, в который будут сохранены результаты: ")
        JsonSaver().save_result(file_name, vacancies.get_raw_data())

        print("Файл с вакансиями успешно создан")


if __name__ == "__main__":
    main()
