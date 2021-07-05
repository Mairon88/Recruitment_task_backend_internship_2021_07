import sys


class ProfilLogger:
    def __init__(self, handlers):
        self.handlers = handlers
        self.info_msg = ''
        self.warning_msg = ''
        self.debug_msg = ''
        self.critical_msg = ''
        self.error_msg = ''
        self.level_msg = ''

    def info(self, msg):
        self.info_msg = str(msg)
        return self.info_msg

    def warning(self, msg):
        self.warning_msg = str(msg)
        return self.warning_msg

    def debug(self, msg):
        self.debug_msg = str(msg)
        return self.debug_msg

    def critical(self, msg):
        self.critical_msg = str(msg)
        return self.critical_msg

    def error(self, msg):
        self.error_msg = str(msg)
        return self.error_msg

    def set_log_level(self, msg):
        msg = msg.upper()
        try:
            if msg not in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:
                raise Exception("WARNINGS: Entered wrong log level")
            self.level_msg = str(msg)
            return self.level_msg
        except Exception:
            print(sys.exc_info()[1])
