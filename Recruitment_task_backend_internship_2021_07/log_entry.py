class LogEntry:
    logs = []

    def __init__(self, date, level, msg):
        self.date = date
        self.level = level
        self.msg = msg
        LogEntry.logs.append([date, level, msg])

    @classmethod
    def reset_logs(cls):
        cls.logs = []




