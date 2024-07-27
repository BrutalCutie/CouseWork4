import os

from config import DATA_PATH
from src.file_saver import JsonSaver


def test_json_saver():
    filename = "test"
    JsonSaver().save_result(filename, [{"dict": "test"}])
    file_path = os.path.join(DATA_PATH, f"{filename}.json")
    assert os.path.exists(file_path)
    os.remove(file_path)
