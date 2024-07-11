import json


class GetJob:
    pass


class HHJobs(GetJob):

    def __init__(self, file_path):
        # TODO не забыть убрать заглушку на requests

        with open(file_path, 'r', encoding='utf8') as file:
            self.__file_data = json.load(file)

    @property
    def file_data(self):
        return json.dumps(self.__file_data, ensure_ascii=False, indent=4)

    @file_data.setter
    def file_data(self, value):
        raise ValueError("Access Denied!")


if __name__ == '__main__':

    getter = HHJobs('../data/vacancies.json')

    print(getter.file_data)
