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
        return f"""
{" Вакансия ":=^100}
Название вакансии: {self.name} 
Требование к вакансии: {self.requirements}
Требуемый опыт: {self.experience}
Запрлата: {f"от {self.salary_from}" if self.salary_from else ''} {f"до {self.salary_to}" if self.salary_to else ''} Руб.
Дата размещения: {self.opened_at}

Описание: {f"{self.descr}" if self.descr else "Отсутствует"}

Адрес: {self.address}
Ссылка на вакансию: {self.vac_url}
{" Конец вакансии ":=^100}
"""[1:]


if __name__ == '__main__':

    with open('../data/vacancies.json', 'r', encoding='utf8') as vacancies:
        vac_data = json.load(vacancies)['items']

    vacs = []

    for index, i in enumerate(vac_data):


        vacs.append(Vacancy(i))


    for i in vacs:
        print(i)
