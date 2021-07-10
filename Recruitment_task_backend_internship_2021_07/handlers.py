import json
import csv
import sqlite3
import os

class JsonHandler:
    def __init__(self, path):
        self.path = path

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
                json_list = json.dumps(list)
                with open(self.path, 'w') as file:
                    file.write(json_list)

            else:
                data.append(list[0])
                with open(self.path, 'w') as file:
                    json.dump(data, file, indent=2)


    def read(self):
        print("Wczytuje dane json")
        if os.path.exists(self.path):
            with open(self.path, 'r') as file:
                logs = json.load(file)
            return logs



class CSVHandler:
    def __init__(self, path):
        self.path = path

    def write(self, list):
        with open(self.path, 'a', encoding='UTF8', newline='') as file:
            data = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            data.writerow(list[0])

    def read(self):
        print("Wczytuje dane csv")
        if os.path.exists(self.path):
            with open(self.path, 'r', encoding='UTF8', newline='') as file:
                reader = csv.reader(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                logs = list(reader)
                return logs

class SQLLiteHandler:
    def __init__(self, path):
        self.path = path

    def write(self, list):
        if not os.path.exists(self.path):
            conn = sqlite3.connect('logs.sqlite')
            c = conn.cursor()
            c.execute('''CREATE TABLE logs
                         (date DATE, level INTEGER, message TEXT)''')

            c.execute("""INSERT INTO logs VALUES (?,?,?)""",
                    (list[0][0], list[0][1], list[0][2]))
            conn.commit()
            conn.close()

        else:
            conn = sqlite3.connect('logs.sqlite')
            c = conn.cursor()
            c.execute("""INSERT INTO logs VALUES (?,?,?)""",
                    (list[0][0], list[0][1], list[0][2]))
            conn.commit()
            conn.close()


    def read(self):
        print("Wczytuje dane sqlite")
        if os.path.exists(self.path):
            conn = sqlite3.connect('logs.sqlite')
            c = conn.cursor()
            logs = [list(row) for row in c.execute('SELECT * FROM logs')]
            conn.close()
            return logs


class FileHandler:
    def __init__(self, path):
        self.path = path

    def write(self, list):
        with open(self.path, 'a') as file:
            file.write((f"{list[0][0]} {list[0][1]} {list[0][2]}"))
            file.write("\n")

    def read(self):
        print("Wczytuje dane txt")
        logs = []
        if os.path.exists(self.path):
            with open(self.path, 'r') as file:
                for log in file:
                    log = log.rstrip('\n').split()
                    logs.append([str(log[0]+' '+log[1]), log[2], ' '.join(log[3:])])

            return logs


