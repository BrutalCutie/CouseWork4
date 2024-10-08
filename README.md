# Парсер вакансий с сайта HH.ru

## Установка
Копирование проекта к себе:
```commandline
git clone https://github.com/BrutalCutie/CouseWork4.git
```
В проекте используется poetry, поэтому для установки используйте:
```commandline
poetry istall
```



# Работа парсера
Для запуска программы наберите в консоли:
```commandline
python main.py
```
Отвечайте на вопросы программы, чтобы получить вакансии результатом.

# Программа умеет:
### Парсить вакансии с сайта www.HH.ru по критериям:
1. Поисковой запрос
2. Поиск по городу
3. Желаемая заработная плата
4. Поиск по ключевым словам 
5. Сохранять полученные вакансии в файл

Максимальное количество вакансий за один поиск: 2000

# Информация по сохраняемым вакансиям
Вакансии сохраняются в папку data с тем названием, который вы укажите, с расширением json

# Пользование
Для получения всех вакансий достаточно инициализировать класс HHJobs из src.vacancies_getter
```
from src.vacancies_getter import HHJobs

all_vacancies = HHJobs(
                    city: str = "ВАШ ГОРОД",  # можно не указывать, тогда поиск будет по всем городам
                    search_field: str = "ВАШ ЗАПРОС В СТРОКЕ ПОИСКА",  # обязательное поле
                    top: int = "ВЫВОД ТОП ВАКАНСИЙ(количество)"  # можно не указывать, будут выведены все
```

Для вывода вакансий в сыром виде(список словарей с данными о вакансиях)
```
print(all_vacancies.get_raw_data())
```
Фильтрация по зарплате
```
filtered_by_salary = all_vacancies.filter_by_salary(salary: str = "ЖЕЛАЕМАЯ МИН ЗАРПЛАТА ИЛИ ДИАПОЗОН ЧЕРЕЗ -)"
```

Фильтрация по ключевым словам в описании
```
filtered_by_keywords = all_vacancies.filter_by_keywords(keywords:str = "КЛЮЧЕВЫЕ СЛОВА ЧЕРЕЗ ПРОБЕЛ)"
```

Так как часть вакансий может быть отсечена в процессе работы, для восстановления из в первоначальный вид
```
all_vacancies.reset_to_primary()
```

Метод as_vacancy_class вернёт список классов Vacancy. __ str __ у Vacancy делает вывод на консоль более читаемым

```
vacs = all_vacancies.as_vacancy_class()

for vac in vacs:
    print(vac)
```

# Тестирование
### Для запуска тестов
```
pytest
```
### Для запуска тестов с информацией о покрытии
```
pytest --cov
```

# В новых версиях:
- ### Возможность работы с базами данных
- ### Многопоточность


