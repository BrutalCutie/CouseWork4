import json
import os.path
from abc import ABC, abstractmethod
from typing import Literal

from config import DATA_PATH


class FileSaver(ABC):

    @abstractmethod
    def save_result(self, *args: tuple, **kwargs: dict):
        pass


class JsonSaver(FileSaver):
    def save_result(self, file_name: str, data: list[dict], method: Literal["w", "a"] = "w", encoding="utf8"):
        """
        Функция для созданения файла формата json в папке data с указанным в file_name названием
        :param file_name: Название файла
        :param data: Передаваемые данные
        :param method: Методы: 'w' - перезапись, 'a' - добавление данных к уже существующим
        :param encoding: Кодировка записи данных
        :return:
        """

        with open(os.path.join(DATA_PATH, file_name + ".json"), method, encoding=encoding) as file:
            file.write(json.dumps(data, ensure_ascii=False, indent=4))
