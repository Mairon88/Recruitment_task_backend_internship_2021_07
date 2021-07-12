import datetime
import sys
import re
import calendar
import pprint

class ProfilLoggerReader:

    """
    A class to read data from files as specified in the method
    The class takes hendlers as a parameter, thanks to which it reads logs from all files to which
    a specific hendler refers
    """

    def __init__(self, handler):

        self.handler = handler
        self.load_data = self.handler.read()
        self.months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        self.levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']

    def find_by_text(self, text, start_date=None, end_date=None):

        """
        The method finds log entries that contain the specified text and print them.
        If any datetime is given, filter logs according to that datetime.
        :param text: the text to find in the log message
        :param start_date: start date of the log range
        :param end_date: end date of the log range
        :return: founded logs
        """

        if self.load_data:
            if start_date and end_date:
                ProfilLoggerReader.dates_validation(start_date, end_date)

                start_date = datetime.datetime.strptime(start_date, "%d-%m-%Y %H:%M:%S")
                end_date = datetime.datetime.strptime(end_date, "%d-%m-%Y %H:%M:%S")
                logs = [log for log in self.load_data if text in log[2] and start_date <=
                        datetime.datetime.strptime(log[0], "%d-%m-%Y %H:%M:%S") <= end_date]
            else:
                logs = [log for log in self.load_data if text in log[2]]
            print("\nLOGS FOUND BY TEXT")
            pprint.pprint(logs)

        else:
            print("No logs")


    def find_by_regex(self, regex, start_date=None, end_date=None):
        """
        The method finds logs by a given regexp and print them.
        If any datetime is given, filter logs according to that datetime.
        :param regex: the regex to find in the log message
        :param start_date: start date of the log range
        :param end_date: end date of the log range
        :return: founded logs
        """
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
            print("\nLOGS FOUND BY REGEX")
            pprint.pprint(logs)

        else:
            print("No logs")


    def groupby_level(self, start_date=None, end_date=None):
        """
         The method groups logs by level and print them.
         If any datetime is given, filter logs according to that datetime.
         :param start_date: start date of the log range
         :param end_date: end date of the log range
         :return: founded logs
         """
        if self.load_data:
            groupby_level_dict = {level:[] for level in self.levels}

            if start_date and end_date:
                ProfilLoggerReader.dates_validation(start_date, end_date)
                start_date = datetime.datetime.strptime(start_date, "%d-%m-%Y %H:%M:%S")
                end_date = datetime.datetime.strptime(end_date, "%d-%m-%Y %H:%M:%S")


                for log in self.load_data:
                    if start_date <= datetime.datetime.strptime(log[0], "%d-%m-%Y %H:%M:%S") <= end_date:
                        groupby_level_dict[log[1]].append(log)

            else:
                for log in self.load_data:
                    groupby_level_dict[log[1]].append(log)
            print("\nLOGS GROUPED BY LEVEL")
            pprint.pprint(groupby_level_dict, sort_dicts=False)

        else:
            print("No logs")

    def groupby_month(self, start_date=None, end_date=None):
        """
         The method groups logs by month and print them.
         If any datetime is given, filter logs according to that datetime.
         :param start_date: start date of the log range
         :param end_date: end date of the log range
         :return: founded logs
         """


        if self.load_data:
            groupby_month_dict = {month: [] for month in self.months}

            if start_date and end_date:

                ProfilLoggerReader.dates_validation(start_date, end_date)
                start_date = datetime.datetime.strptime(start_date, "%d-%m-%Y %H:%M:%S")
                end_date = datetime.datetime.strptime(end_date, "%d-%m-%Y %H:%M:%S")

                for log in self.load_data:
                    if start_date <= datetime.datetime.strptime(log[0], "%d-%m-%Y %H:%M:%S") <= end_date:
                        groupby_month_dict[calendar.month_name[int(log[0][3:5])]].append(log)

            else:
                for log in self.load_data:
                    groupby_month_dict[calendar.month_name[int(log[0][3:5])]].append(log)
            print("\nLOGS GROUPED BY MONTH")
            pprint.pprint(groupby_month_dict, sort_dicts=False)

        else:
            print("No logs")


    @staticmethod
    def dates_validation(start_date, end_date):
        """
        The method to validation entered dates.
        :param start_date: start date of the log range
        :param end_date: end date of the log range
        """
        try:
            start_date = datetime.datetime.strptime(start_date, "%d-%m-%Y %H:%M:%S")
            end_date = datetime.datetime.strptime(end_date, "%d-%m-%Y %H:%M:%S")
            if start_date > end_date:
                raise Exception("WARNING: Start date should be earlier than end date")

        except Exception:
            print(sys.exc_info()[1])
            sys.exit()
