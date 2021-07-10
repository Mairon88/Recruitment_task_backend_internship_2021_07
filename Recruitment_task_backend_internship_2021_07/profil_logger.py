import sys
from .log_entry import LogEntry
from datetime import datetime
import inspect


class ProfilLogger:

    """
    Class for creating logs in the form of a list with creation date,
    level and information.
    The class takes hendlers as a parameter, thanks to which it writes logs to all files to which
    a specific hendler refers
    """
    levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    level = None

    def __init__(self, handlers):
        self.handlers = handlers
        self.info_msg = ''
        self.warning_msg = ''
        self.debug_msg = ''
        self.critical_msg = ''
        self.error_msg = ''

    def info(self, msg):
        """
        The method creates a log with the INFO level
        :param msg: information transmitted in the log
        """
        self.info_msg = str(msg)
        ProfilLogger.save_logs(inspect.stack()[0][3],self.info_msg, self.handlers)


    def warning(self, msg):
        """
        The method creates a log with the WARNING level
:       param msg: information transmitted in the log
        """
        self.warning_msg = str(msg)
        ProfilLogger.save_logs(inspect.stack()[0][3], self.warning_msg, self.handlers)

    def debug(self, msg):
        """
        The method creates a log with the DEBUG level
        :param msg: information transmitted in the log
        """
        self.debug_msg = str(msg)
        ProfilLogger.save_logs(inspect.stack()[0][3], self.info_msg, self.handlers)

    def critical(self, msg):
        """
        The method creates a log with the CRITICAL level
        :param msg: information transmitted in the log
        """
        self.critical_msg = str(msg)
        ProfilLogger.save_logs(inspect.stack()[0][3], self.critical_msg, self.handlers)

    def error(self, msg):
        """
        The method creates a log with the ERROR level
        :param msg: information transmitted in the log
        """

        self.error_msg = str(msg)
        ProfilLogger.save_logs(inspect.stack()[0][3], self.error_msg, self.handlers)

    @classmethod
    def save_logs(cls,level, msg, handlers):
        """
        Class method to write logs by calling each of the given handlers
        :param level: level transmitted in the log
        :param msg: information transmitted in the log
        :param handlers: handlers used to write to the file
        :return:
        """

        if ProfilLogger.check_levels(level.upper()):
            log = LogEntry(cls.now, level.upper(), msg)
            for handler in handlers:
                handler.write(log.logs)
            LogEntry.reset_logs()


    @classmethod
    def set_log_level(cls,level='DEBUG'):
        """
        Class method to set minimal log level to be saved
        :param level: log level to be set
        :return: level
        """
        try:
            if level not in cls.levels:
                raise Exception("WARNING: Entered wrong log level, the available levels are: "
                                "'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL' ")
            else:
                cls.level = str(level)
                return ProfilLogger.level
        except Exception:
            print(sys.exc_info()[1])
            sys.exit()

    @classmethod
    def check_levels(cls,current_level):
        """
        Class method to compare the set level with the log levels
        :param current_level:
        :return: True
        """
        if cls.levels.index(current_level) >= cls.levels.index(cls.level):
            return True



