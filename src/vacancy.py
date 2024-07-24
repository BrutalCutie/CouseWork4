import json


class Vacancy:

    def __init__(self, vacancy_data: dict):
        self.vacancy_data = vacancy_data
        self.name: str | None = vacancy_data.get('name')
        self.descr: str | None = vacancy_data.get('snippet', {}).get('responsibility')
        self.requirements: str | None = vacancy_data.get('snippet', {}).get('requirement')
        self.experience: str | None = vacancy_data.get("experience", {}).get("name")

        self.address: dict | None = vacancy_data.get('address')
        if self.address:
            self.address = self.address.get("raw")
        else:
            self.address = 'Не указан'

        self.opened_at: str | None = vacancy_data.get("published_at")
        self.salary_group: dict = vacancy_data.get('salary', {})
        self.salary_from: int | None = self.salary_group.get('from')
        self.salary_to: int | None = self.salary_group.get('to')
        self.vac_url: str = vacancy_data.get('alternate_url')

    def __str__(self):
        return (f"{" Вакансия ":=^100}\n"
                f"Название вакансии: {self.name}\n"
                f"Требование к вакансии: {self.requirements}\n"
                f"Требуемый опыт: {self.experience}\n"
                f"Запрлата: {f"от {self.pretty_salary(self.salary_from)}" if self.salary_from else ''} "
                f"{f"до {self.pretty_salary(self.salary_to)}" if self.salary_to else ''} Руб.\n"
                f"Дата размещения: {self.opened_at}\n"
                f"Описание: {f"{self.descr}" if self.descr else "Отсутствует"}\n"
                f"Адрес: {self.address}\n"
                f"Ссылка на вакансию: {self.vac_url}\n"
                f"{" Конец вакансии ":=^100}\n")

    def __gt__(self, other):
        if isinstance(other, Vacancy):
            my_salary = self.salary_from or self.salary_to
            other_salary = other.salary_from or other.salary_to
            return my_salary > other_salary

        raise TypeError('Для сравнения должен быть использован Vacancy')

    def __ge__(self, other):
        if isinstance(other, Vacancy):
            my_salary = self.salary_from or self.salary_to
            other_salary = other.salary_from or other.salary_to
            return my_salary >= other_salary

        raise TypeError('Для сравнения должен быть использован Vacancy')

    def __eq__(self, other):
        if isinstance(other, Vacancy):
            my_salary = self.salary_from or self.salary_to
            other_salary = other.salary_from or other.salary_to
            return my_salary == other_salary
        raise TypeError('Для сравнения должен быть использован Vacancy')

    @staticmethod
    def pretty_salary(value: int | None) -> str | None:
        """
        Функция для красивого отображения зарплаты Пример: value=100000, преобразуем в 100 000, что приятнее глазу
        :param value: Число, которое будет оформлено
        :return:
        """
        if isinstance(value, int):
            value = str(value)[::-1]
            text = ""
            for index, numb in enumerate(value, 1):
                text += numb

                if index % 3 == 0 and len(value) != index:
                    text += ' '
            return text[::-1]
        return value


if __name__ == '__main__':

    # with open('../data/vacancies.json', 'r', encoding='utf8') as vacancies:
    #     vac_data = json.load(vacancies)['items']
    #
    # vacs = []
    #
    # for index, i in enumerate(vac_data):
    #
    #     vacs.append(Vacancy(i))
    #
    #
    # for i in vacs:
    #     print(i)
    vac1 = Vacancy({
        'salary': {
            'from': 10000
        }
    })

    vac2 = Vacancy({
        'salary': {
            'from': 10000
        }
    })

    print(vac2 == vac1)

