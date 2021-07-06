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
        if ProfilLogger.check_levels('INFO'):
            log = LogEntry(ProfilLogger.now, 'INFO', self.info_msg)
            # for handler in self.handlers:
            #     handler.write(log.logs)
            self.handlers[0].write(log.logs)
            self.handlers[1].write(log.logs)
            LogEntry.reset_logs()


    def warning(self, msg):
        self.warning_msg = str(msg)
        if ProfilLogger.check_levels('WARNING'):
            log = LogEntry(ProfilLogger.now, 'WARNING', self.warning_msg)
            self.handlers[0].write(log.logs)
            self.handlers[1].write(log.logs)
            LogEntry.reset_logs()

    def debug(self, msg):
        self.debug_msg = str(msg)
        if ProfilLogger.check_levels('DEBUG'):
            log = LogEntry(ProfilLogger.now, 'DEBUG', self.debug_msg)
            self.handlers[0].write(log.logs)
            self.handlers[1].write(log.logs)
            LogEntry.reset_logs()


    def critical(self, msg):
        self.critical_msg = str(msg)
        if ProfilLogger.check_levels('CRITICAL'):
            log = LogEntry(ProfilLogger.now, 'CRITICAL', self.critical_msg)
            self.handlers[0].write(log.logs)
            self.handlers[1].write(log.logs)
            LogEntry.reset_logs()



    def error(self, msg):
        self.error_msg = str(msg)
        if ProfilLogger.check_levels('ERROR'):
            log = LogEntry(ProfilLogger.now, 'ERROR', self.error_msg)
            self.handlers[0].write(log.logs)
            self.handlers[1].write(log.logs)
            LogEntry.reset_logs()



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


    @staticmethod
    def check_levels(current_level):
        if ProfilLogger.levels.index(current_level) >= ProfilLogger.levels.index(ProfilLogger.level):
            return True

