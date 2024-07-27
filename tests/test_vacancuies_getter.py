from src.vacancies_getter import HHJobs
from unittest.mock import patch

from src.vacancy import Vacancy


@patch("requests.get")
def test_raw_data(mock_get):
    mock_get.return_value.json.return_value = {
        "items": [
            {
                "address": {
                    "building": "9с10",
                    "city": "Москва",
                    "description": "На проходной потребуется паспорт",
                    "lat": 55.807794,
                    "lng": 37.638699,
                    "metro_stations": [
                        {
                            "lat": 55.807794,
                            "line_id": "6",
                            "line_name": "Калужско-Рижская",
                            "lng": 37.638699,
                            "station_id": "6.8",
                            "station_name": "Алексеевская",
                        }
                    ],
                    "street": "улица Годовикова",
                },
                "alternate_url": "https://hh.ru/vacancy/8331228",
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=8331228",
                "area": {"id": "1", "name": "Москва", "url": "https://api.hh.ru/areas/1"},
                "brand_snippet": {
                    "background": {
                        "color": None,
                        "gradient": {
                            "angle": 45,
                            "color_list": [{"color": "#FF0000", "position": 10}, {"color": "#FA0000", "position": 9}],
                        },
                    },
                    "logo": "https://hhcdn.ru/00001.png",
                    "logo_scalable": {
                        "default": {"height": 300, "url": "https://hhcdn.ru/00021.png", "width": 500},
                        "xs": {"height": 100, "url": "https://hhcdn.ru/00022.png", "width": 200},
                    },
                    "logo_xs": "https://hhcdn.ru/00002.png",
                    "picture": "https://hhcdn.ru/00003.png",
                    "picture_scalable": {
                        "default": {"height": 350, "url": "https://hhcdn.ru/00023.png", "width": 550},
                        "xs": {"height": 150, "url": "https://hhcdn.ru/00024.png", "width": 250},
                    },
                    "picture_xs": "https://hhcdn.ru/00004.png",
                },
                "branding": {"tariff": "BASIC", "type": "CONSTRUCTOR"},
                "contacts": {
                    "email": "user@example.com",
                    "name": "Имя",
                    "phones": [{"city": "985", "comment": None, "country": "7", "number": "000-00-00"}],
                },
                "counters": {"responses": 0},
                "department": {"id": "HH-1455-TECH", "name": "HeadHunter::Технический департамент"},
                "employer": {
                    "accredited_it_employer": False,
                    "alternate_url": "https://hh.ru/employer/1455",
                    "id": "1455",
                    "logo_urls": {
                        "90": "https://hh.ru/employer-logo/289027.png",
                        "240": "https://hh.ru/employer-logo/289169.png",
                        "original": "https://hh.ru/file/2352807.png",
                    },
                    "name": "HeadHunter",
                    "trusted": True,
                    "url": "https://api.hh.ru/employers/1455",
                },
                "has_test": True,
                "id": "8331228",
                "insider_interview": {"id": "12345", "url": "https://hh.ru/interview/12345?employerId=777"},
                "name": "Секретарь",
                "personal_data_resale": False,
                "professional_roles": [{"id": "90", "name": "Охранник"}],
                "published_at": "2013-07-08T16:17:21+0400",
                "relations": [],
                "response_letter_required": True,
                "response_url": None,
                "salary": {"currency": "RUR", "from": 30000, "gross": True, "to": None},
                "schedule": {"id": "fullDay", "name": "Полный день"},
                "show_logo_in_search": True,
                "snippet": {
                    "requirement": "Высшее образование. Опыт работы в качестве <highlighttext>секретаря</highlighttext>, офис-менеджера. Знание делопроизводства, документооборота. Коммуникативные навыки.",
                    "responsibility": "Документооборот (регистрация, отправка, контроль исполнения писем, ведение протоколов, отчетность). Распределение корреспонденции. Прием и распределение телефонных звонков.",
                },
                "sort_point_distance": 226.001293,
                "type": {"id": "open", "name": "Открытая"},
                "url": "https://api.hh.ru/vacancies/8331228",
            }
        ],
        "page": 0,
        "pages": 0,
        "per_page": 100,
    }

    all_vacs = HHJobs("уфа", "HeadHunter", 5)
    data = [
        {
            "address": {
                "building": "9с10",
                "city": "Москва",
                "description": "На проходной потребуется паспорт",
                "lat": 55.807794,
                "lng": 37.638699,
                "metro_stations": [
                    {
                        "lat": 55.807794,
                        "line_id": "6",
                        "line_name": "Калужско-Рижская",
                        "lng": 37.638699,
                        "station_id": "6.8",
                        "station_name": "Алексеевская",
                    }
                ],
                "street": "улица Годовикова",
            },
            "alternate_url": "https://hh.ru/vacancy/8331228",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=8331228",
            "area": {"id": "1", "name": "Москва", "url": "https://api.hh.ru/areas/1"},
            "brand_snippet": {
                "background": {
                    "color": None,
                    "gradient": {
                        "angle": 45,
                        "color_list": [{"color": "#FF0000", "position": 10}, {"color": "#FA0000", "position": 9}],
                    },
                },
                "logo": "https://hhcdn.ru/00001.png",
                "logo_scalable": {
                    "default": {"height": 300, "url": "https://hhcdn.ru/00021.png", "width": 500},
                    "xs": {"height": 100, "url": "https://hhcdn.ru/00022.png", "width": 200},
                },
                "logo_xs": "https://hhcdn.ru/00002.png",
                "picture": "https://hhcdn.ru/00003.png",
                "picture_scalable": {
                    "default": {"height": 350, "url": "https://hhcdn.ru/00023.png", "width": 550},
                    "xs": {"height": 150, "url": "https://hhcdn.ru/00024.png", "width": 250},
                },
                "picture_xs": "https://hhcdn.ru/00004.png",
            },
            "branding": {"tariff": "BASIC", "type": "CONSTRUCTOR"},
            "contacts": {
                "email": "user@example.com",
                "name": "Имя",
                "phones": [{"city": "985", "comment": None, "country": "7", "number": "000-00-00"}],
            },
            "counters": {"responses": 0},
            "department": {"id": "HH-1455-TECH", "name": "HeadHunter::Технический департамент"},
            "employer": {
                "accredited_it_employer": False,
                "alternate_url": "https://hh.ru/employer/1455",
                "id": "1455",
                "logo_urls": {
                    "240": "https://hh.ru/employer-logo/289169.png",
                    "90": "https://hh.ru/employer-logo/289027.png",
                    "original": "https://hh.ru/file/2352807.png",
                },
                "name": "HeadHunter",
                "trusted": True,
                "url": "https://api.hh.ru/employers/1455",
            },
            "has_test": True,
            "id": "8331228",
            "insider_interview": {"id": "12345", "url": "https://hh.ru/interview/12345?employerId=777"},
            "name": "Секретарь",
            "personal_data_resale": False,
            "professional_roles": [{"id": "90", "name": "Охранник"}],
            "published_at": "2013-07-08T16:17:21+0400",
            "relations": [],
            "response_letter_required": True,
            "response_url": None,
            "salary": {"currency": "RUR", "from": 30000, "gross": True, "to": None},
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "show_logo_in_search": True,
            "snippet": {
                "requirement": "Высшее образование. Опыт работы в качестве "
                "<highlighttext>секретаря</highlighttext>, "
                "офис-менеджера. Знание делопроизводства, "
                "документооборота. Коммуникативные навыки.",
                "responsibility": "Документооборот (регистрация, отправка, "
                "контроль исполнения писем, ведение "
                "протоколов, отчетность). Распределение "
                "корреспонденции. Прием и распределение "
                "телефонных звонков.",
            },
            "sort_point_distance": 226.001293,
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/8331228",
        }
    ]
    assert all_vacs.get_raw_data() == data
    assert all_vacs.filter_by_salary("5000000-100000000").get_raw_data() == []
    all_vacs.reset_to_primary()
    assert all_vacs.get_raw_data() == data

    assert all_vacs.filter_by_keywords("контроль").get_raw_data() == data
    all_vacs.reset_to_primary()
    assert all_vacs.filter_by_keywords("тест").get_raw_data() == []

    all_vacs.reset_to_primary()

    assert all_vacs.as_vacancy_class()[0].__class__ == Vacancy
