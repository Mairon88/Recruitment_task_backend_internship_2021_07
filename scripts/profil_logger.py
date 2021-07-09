import sys
from log_entry import LogEntry
from datetime import datetime
import inspect


class ProfilLogger:
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
        self.info_msg = str(msg)
        ProfilLogger.save_logs(inspect.stack()[0][3],self.info_msg, self.handlers)


    def warning(self, msg):
        self.warning_msg = str(msg)
        ProfilLogger.save_logs(inspect.stack()[0][3], self.warning_msg, self.handlers)

    def debug(self, msg):
        self.debug_msg = str(msg)
        ProfilLogger.save_logs(inspect.stack()[0][3], self.info_msg, self.handlers)


    def critical(self, msg):
        self.critical_msg = str(msg)
        ProfilLogger.save_logs(inspect.stack()[0][3], self.critical_msg, self.handlers)

    def error(self, msg):
        self.error_msg = str(msg)
        ProfilLogger.save_logs(inspect.stack()[0][3], self.error_msg, self.handlers)

    @classmethod
    def save_logs(cls,level, msg, handlers):
        if ProfilLogger.check_levels(level.upper()):
            log = LogEntry(cls.now, level.upper(), msg)
            for handler in handlers:
                handler.write(log.logs)
            LogEntry.reset_logs()

    @classmethod
    def set_log_level(cls,msg='DEBUG'):
        try:
            if msg not in cls.levels:
                raise Exception("WARNING: Entered wrong log level, the available levels are: "
                                "'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL' ")
            else:
                cls.level = str(msg)
                return ProfilLogger.level
        except Exception:
            print(sys.exc_info()[1])
            sys.exit()

    @classmethod
    def check_levels(cls,current_level):
        if cls.levels.index(current_level) >= cls.levels.index(cls.level):
            return True



