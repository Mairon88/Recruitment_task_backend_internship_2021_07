import json
import csv
import sqlite3
import os

class JsonHandler:

    """
    Class for reading and writing to a json file,
    takes the path to the file as a parameter
    """

    def __init__(self, path):
        self.path = path

    def write(self, data_list):

        """
        The method saves the log list in the json file

        :param data_list: List with logs to write in file
        :return: None
        """

        json_list = json.dumps(data_list)
        print(json_list)
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
                json_list = json.dumps(data_list)
                with open(self.path, 'w') as file:
                    file.write(json_list)

            else:
                data.append(data_list[0])
                with open(self.path, 'w') as file:
                    json.dump(data, file, indent=2)


    def read(self):

        """
        The method loads the log list from the json file

        :return: List with logs
        """

        if os.path.exists(self.path):
            with open(self.path, 'r') as file:
                logs = json.load(file)
            return logs



class CSVHandler:

    """
    The method saves the log list in the csv file

    :param data_list: List with logs to write in file
    :return: None
    """

    def __init__(self, path):
        self.path = path

    def write(self, data_list):

        """
        The method saves the log list in the sql file

        :param data_list: List with logs to write in file
        :return: None
        """

        with open(self.path, 'a', encoding='UTF8', newline='') as file:
            data = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            data.writerow(data_list[0])

    def read(self):

        """
        The method loads the log list from the csv file

        :return: List with logs
        """
        if os.path.exists(self.path):
            with open(self.path, 'r', encoding='UTF8', newline='') as file:
                reader = csv.reader(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                logs = list(reader)
                return logs

class SQLLiteHandler:

    """
    Class for reading and writing to a sqlite file,
    takes the path to the file as a parameter
    """

    def __init__(self, path):
        self.path = path

    def write(self, data_list):

        """
        The method saves the log list in the sql file

        :param data_list: List with logs to write in file
        :return: None
        """

        if not os.path.exists(self.path):
            conn = sqlite3.connect(self.path)
            c = conn.cursor()
            c.execute('''CREATE TABLE logs
                         (date DATE, level INTEGER, message TEXT)''')

            c.execute("""INSERT INTO logs VALUES (?,?,?)""",
                    (data_list[0][0], data_list[0][1], data_list[0][2]))
            conn.commit()
            conn.close()

        else:
            conn = sqlite3.connect(self.path)
            c = conn.cursor()
            c.execute("""INSERT INTO logs VALUES (?,?,?)""",
                    (data_list[0][0], data_list[0][1], data_list[0][2]))
            conn.commit()
            conn.close()


    def read(self):

        """
        The method loads the log list from the sql file

        :return: List with logs
        """

        if os.path.exists(self.path):
            conn = sqlite3.connect(self.path)
            c = conn.cursor()
            logs = [list(row) for row in c.execute('SELECT * FROM logs')]
            conn.close()
            return logs


class FileHandler:

    """
    Class for reading and writing to a txt file,
    takes the path to the file as a parameter
    """

    def __init__(self, path):
        self.path = path

    def write(self, data_list):

        """
        The method saves the log list in the txt file

        :param data_list: List with logs to write in file
        :return: None
        """

        with open(self.path, 'a') as file:
            file.write((f"{data_list[0][0]} {data_list[0][1]} {data_list[0][2]}"))
            file.write("\n")

    def read(self):

        """
        The method loads the log list from the txt file

        :return: List with logs
        """

        logs = []
        if os.path.exists(self.path):
            with open(self.path, 'r') as file:
                for log in file:
                    log = log.rstrip('\n').split()
                    logs.append([str(log[0]+' '+log[1]), log[2], ' '.join(log[3:])])

            return logs


