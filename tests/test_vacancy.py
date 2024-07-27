import pytest
from src.vacancy import Vacancy


def test_vacancy_without_city(capsys):
    vac_data = {
        "id": "98707107",
        "premium": False,
        "name": "Разработчик С++",
        "department": None,
        "has_test": False,
        "response_letter_required": False,
        "area": {"id": "99", "name": "Уфа", "url": "https://api.hh.ru/areas/99"},
        "salary": {"from": 300000, "to": None, "currency": "RUR", "gross": True},
        "type": {"id": "open", "name": "Открытая"},
        "address": None,
        "response_url": None,
        "sort_point_distance": None,
        "published_at": "2024-05-11T17:53:15+0300",
        "created_at": "2024-05-11T17:53:15+0300",
        "archived": True,
        "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=98707107",
        "show_logo_in_search": None,
        "insider_interview": None,
        "url": "https://api.hh.ru/vacancies/98707107?host=hh.ru",
        "alternate_url": "https://hh.ru/vacancy/98707107",
        "relations": [],
        "employer": {
            "id": "10384591",
            "name": "Лаборатория Современных Цифровых Технологий",
            "url": "https://api.hh.ru/employers/10384591",
            "alternate_url": "https://hh.ru/employer/10384591",
            "logo_urls": {
                "240": "https://img.hhcdn.ru/employer-logo/6601822.jpeg",
                "90": "https://img.hhcdn.ru/employer-logo/6601821.jpeg",
                "original": "https://img.hhcdn.ru/employer-logo-original/1245348.jpg",
            },
            "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10384591",
            "accredited_it_employer": True,
            "trusted": True,
        },
        "snippet": {"requirement": None, "responsibility": None},
        "contacts": None,
        "schedule": {"id": "fullDay", "name": "Полный день"},
        "working_days": [],
        "working_time_intervals": [],
        "working_time_modes": [],
        "accept_temporary": False,
        "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
        "accept_incomplete_resumes": False,
        "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
        "employment": {"id": "full", "name": "Полная занятость"},
        "adv_response_url": None,
        "is_adv_vacancy": False,
        "adv_context": None,
    }
    print(Vacancy(vacancy_data=vac_data))
    captured = capsys.readouterr()

    assert (
        captured.out
        == """
============================================= Вакансия =============================================
Название вакансии: Разработчик С++
Требование к вакансии: None
Требуемый опыт: От 1 года до 3 лет
Запрлата: от 300 000  Руб.
Дата размещения: 2024-05-11T17:53:15+0300
Описание: Отсутствует
Адрес: Не указан
Ссылка на вакансию: https://hh.ru/vacancy/98707107
========================================== Конец вакансии ==========================================

"""[
            1:
        ]
    )


def test_vacancy_with_city(capsys):
    vac_data = {
        "id": "98707107",
        "premium": False,
        "name": "Разработчик С++",
        "department": None,
        "has_test": False,
        "response_letter_required": False,
        "area": {"id": "99", "name": "Уфа", "url": "https://api.hh.ru/areas/99"},
        "salary": {"from": 300000, "to": None, "currency": "RUR", "gross": True},
        "type": {"id": "open", "name": "Открытая"},
        "address": {"raw": "Уфа, улица Джалиля Киекбаева, 2"},
        "response_url": None,
        "sort_point_distance": None,
        "published_at": "2024-05-11T17:53:15+0300",
        "created_at": "2024-05-11T17:53:15+0300",
        "archived": True,
        "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=98707107",
        "show_logo_in_search": None,
        "insider_interview": None,
        "url": "https://api.hh.ru/vacancies/98707107?host=hh.ru",
        "alternate_url": "https://hh.ru/vacancy/98707107",
        "relations": [],
        "employer": {
            "id": "10384591",
            "name": "Лаборатория Современных Цифровых Технологий",
            "url": "https://api.hh.ru/employers/10384591",
            "alternate_url": "https://hh.ru/employer/10384591",
            "logo_urls": {
                "240": "https://img.hhcdn.ru/employer-logo/6601822.jpeg",
                "90": "https://img.hhcdn.ru/employer-logo/6601821.jpeg",
                "original": "https://img.hhcdn.ru/employer-logo-original/1245348.jpg",
            },
            "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10384591",
            "accredited_it_employer": True,
            "trusted": True,
        },
        "snippet": {"requirement": None, "responsibility": None},
        "contacts": None,
        "schedule": {"id": "fullDay", "name": "Полный день"},
        "working_days": [],
        "working_time_intervals": [],
        "working_time_modes": [],
        "accept_temporary": False,
        "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
        "accept_incomplete_resumes": False,
        "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
        "employment": {"id": "full", "name": "Полная занятость"},
        "adv_response_url": None,
        "is_adv_vacancy": False,
        "adv_context": None,
    }
    print(Vacancy(vacancy_data=vac_data))
    captured = capsys.readouterr()

    assert (
        captured.out
        == """
============================================= Вакансия =============================================
Название вакансии: Разработчик С++
Требование к вакансии: None
Требуемый опыт: От 1 года до 3 лет
Запрлата: от 300 000  Руб.
Дата размещения: 2024-05-11T17:53:15+0300
Описание: Отсутствует
Адрес: Уфа, улица Джалиля Киекбаева, 2
Ссылка на вакансию: https://hh.ru/vacancy/98707107
========================================== Конец вакансии ==========================================

"""[
            1:
        ]
    )


def test_vacancy_equal(vac1, vac1_2):
    assert vac1 == vac1_2


def test_vacancy_wrong_type(vac1):
    with pytest.raises(TypeError):
        vac1 == 123


def test_vacancy_gt(vac1, vac2):
    assert vac1 < vac2


def test_vacancy_ge(vac1, vac1_2):
    assert vac1 <= vac1_2
