import os
import json

class JsonActions:


    def __init__(self):
        self.json = json

    def choice_json_file(self, filename):
        return os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "../data/"+filename)  # указали путь для файла

    def read_json_file(self, filename):
        with open(self.choice_json_file(filename), "r", encoding="utf-8") as f:
                data = json.loads(f.read())
                return data

    def write_json_file(self, filename):
        with open(self.choice_json_file(filename), "w", encoding="utf-8") as f:  # открыли файл на запись
            json.dump(dict, f, indent=1, ensure_ascii=False)

