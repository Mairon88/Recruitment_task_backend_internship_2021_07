class LogEntry:
    """
    Class for creating a single log, which is later written to a file
    """
    logs = []

    def __init__(self, date, level, msg):
        self.date = date
        self.level = level
        self.msg = msg
        LogEntry.logs.append([date, level, msg])

    @classmethod
    def reset_logs(cls):
        """
        The method for reset logs
        """
        cls.logs = []




