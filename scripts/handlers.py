import json
import csv
import os

class JsonHandler:
    def __init__(self, path):
        self.path = path
        print("Tworzę plik: 'logs.json'")

    def write(self, list):
        json_list = json.dumps(list)
        if not os.path.exists(self.path):
            with open(self.path, 'w') as file:
                file.write(json_list)
        else:

            with open(self.path, 'r') as file:
                try:
                    is_file_empty = False
                    data = json.load(file)
                except:
                    is_file_empty = True
            if is_file_empty:
                print("JEST PUSTY")
                json_list = json.dumps(list)
                with open(self.path, 'w') as file:
                    file.write(json_list)

            else:
                data.append(list[0])
                with open(self.path, 'w') as file:
                    json.dump(data, file)


    def read(self):
        pass

class CSVHandler:
    def __init__(self, path):
        self.path = path
        print("Tworzę plik: 'logs.csv'")

    def write(self, list):

        with open(self.path, 'a', encoding='UTF8', newline='') as file:
            data = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            data.writerow(list[0])

    def read(self):
        pass

class SQLLiteHandler:
    def __init__(self, path):
        self.path = path
        print("Tworzę plik: 'logs.sqlite'")

    def write(self):
        pass

    def read(self):
        pass

class FileHandler:
    def __init__(self, path):
        self.path = path
        print("Tworzę plik: 'logs.txt'")

    def write(self):


    def read(self):
        pass
