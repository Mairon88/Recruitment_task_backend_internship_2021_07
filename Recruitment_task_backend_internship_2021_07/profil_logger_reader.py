import datetime
import sys
import re
import calendar


class ProfilLoggerReader:

    def __init__(self, handler):

        self.handler = handler
        self.load_data = self.handler.read()

    def find_by_text(self, text, start_date=None, end_date=None):

        logs = []

        if self.load_data:
            if start_date and end_date:
                ProfilLoggerReader.dates_validation(start_date, end_date)

                start_date = datetime.datetime.strptime(start_date, "%d-%m-%Y %H:%M:%S")
                end_date = datetime.datetime.strptime(end_date, "%d-%m-%Y %H:%M:%S")
                logs = [log for log in self.load_data if text in log[2] and start_date <=
                        datetime.datetime.strptime(log[0], "%d-%m-%Y %H:%M:%S") <= end_date]
            else:
                logs = [log for log in self.load_data if text in log[2]]

            return logs

        else:
            return "BRAK DANYCH DO PRACY"


    def find_by_regex(self, regex, start_date=None, end_date=None):

        logs = []

        if self.load_data:
            log_regex = re.compile(regex)

            if start_date and end_date:
                ProfilLoggerReader.dates_validation(start_date, end_date)

                start_date = datetime.datetime.strptime(start_date, "%d-%m-%Y %H:%M:%S")
                end_date = datetime.datetime.strptime(end_date, "%d-%m-%Y %H:%M:%S")

                for log in self.load_data:
                    if log_regex.findall(log[2]):
                        found_log = log_regex.findall(log[2])[0]
                        if found_log in log[2] and \
                                start_date <= datetime.datetime.strptime(log[0], "%d-%m-%Y %H:%M:%S") <= end_date:
                            logs.append(log)

            else:

                for log in self.load_data:
                    if log_regex.findall(log[2]):
                        found_log = log_regex.findall(log[2])[0]
                        if found_log in log[2]:
                            logs.append(log)

            return logs

        else:
            return "BRAK DANYCH DO PRACY"


    def groupby_level(self, start_date=None, end_date=None):

        if self.load_data:
            #Tworzenie kluczy z wartosciami w formie pustych list
            groupby_level_dict = {log[1]:[] for log in self.load_data}

            #Uzupełniani wartosci listami z logami
            if start_date and end_date:
                ProfilLoggerReader.dates_validation(start_date, end_date)
                start_date = datetime.datetime.strptime(start_date, "%d-%m-%Y %H:%M:%S")
                end_date = datetime.datetime.strptime(end_date, "%d-%m-%Y %H:%M:%S")
                groupby_level_dict = {log[1]:[] for log in self.load_data
                                      if start_date <= datetime.datetime.strptime(log[0], "%d-%m-%Y %H:%M:%S")
                                      <= end_date}

                for log in self.load_data:
                    if start_date <= datetime.datetime.strptime(log[0], "%d-%m-%Y %H:%M:%S") <= end_date:
                        groupby_level_dict[log[1]].append(log)

            else:
                for log in self.load_data:
                    groupby_level_dict[log[1]].append(log)

            return groupby_level_dict

        else:
            return "BRAK DANYCH DO PRACY"

    def groupby_month(self, start_date=None, end_date=None):

        if self.load_data:
            groupby_month_dict = {calendar.month_name[int(log[0][3:5])]: [] for log in self.load_data}

            #Uzupełniani wartosci listami z logami
            if start_date and end_date:
                # Tworzenie kluczy nazwami miesięcy i z wartosciami w formie pustych list

                ProfilLoggerReader.dates_validation(start_date, end_date)
                start_date = datetime.datetime.strptime(start_date, "%d-%m-%Y %H:%M:%S")
                end_date = datetime.datetime.strptime(end_date, "%d-%m-%Y %H:%M:%S")
                groupby_month_dict = {calendar.month_name[int(log[0][3:5])]: [] for log in self.load_data
                                      if start_date <= datetime.datetime.strptime(log[0], "%d-%m-%Y %H:%M:%S")
                                      <= end_date}

                for log in self.load_data:
                    if start_date <= datetime.datetime.strptime(log[0], "%d-%m-%Y %H:%M:%S") <= end_date:
                        groupby_month_dict[calendar.month_name[int(log[0][3:5])]].append(log)

            else:
                for log in self.load_data:
                    groupby_month_dict[calendar.month_name[int(log[0][3:5])]].append(log)

            return groupby_month_dict

        else:
            return "BRAK DANYCH DO PRACY"


    @staticmethod
    def dates_validation(start_date, end_date):
        try:
            start_date = datetime.datetime.strptime(start_date, "%d-%m-%Y %H:%M:%S")
            end_date = datetime.datetime.strptime(end_date, "%d-%m-%Y %H:%M:%S")
            if start_date > end_date:
                raise Exception("WARNING: Start date should be earlier than end date")

        except Exception:
            print(sys.exc_info()[1])
            sys.exit()
