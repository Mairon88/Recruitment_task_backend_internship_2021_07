import sys
from log_entry import LogEntry
from datetime import datetime


class ProfilLogger:
    levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
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
        LogEntry(ProfilLogger.now, 'INFO', self.info_msg)
        return self.info_msg

    def warning(self, msg):
        self.warning_msg = str(msg)
        LogEntry(ProfilLogger.now, 'WARNING', self.warning_msg)
        return self.warning_msg

    def debug(self, msg):
        self.debug_msg = str(msg)
        LogEntry(ProfilLogger.now, 'DEBUG', self.debug_msg)
        return self.debug_msg

    def critical(self, msg):
        self.critical_msg = str(msg)
        LogEntry(ProfilLogger.now, 'CRITICAL', self.critical_msg)
        return self.critical_msg

    def error(self, msg):
        self.error_msg = str(msg)
        LogEntry(ProfilLogger.now, 'ERROR', self.error_msg)
        return self.error_msg

    @staticmethod
    def set_log_level(msg='DEBUG'):
        try:
            if msg not in ProfilLogger.levels:
                raise Exception("WARNINGS: Entered wrong log level")
            else:
                ProfilLogger.level = str(msg)
                return ProfilLogger.level
        except Exception:
            print(sys.exc_info()[1])
            sys.exit()
