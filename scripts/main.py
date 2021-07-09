from handlers import JsonHandler, CSVHandler, SQLLiteHandler, FileHandler
from profil_logger import ProfilLogger
from profil_logger_reader import ProfilLoggerReader

json_handler = JsonHandler("logs.json")
csv_handler = CSVHandler("logs.csv")
sql_handler = SQLLiteHandler("logs.sqlite")
file_handler = FileHandler("logs.txt")

handlers = [json_handler, csv_handler, sql_handler, file_handler]

logger = ProfilLogger(handlers)
logger.set_log_level('INFO')
logger.info("Some info message")
logger.warning("Some warning message")
logger.debug("Some debug message")
logger.critical("Some critical message")
logger.error("Some error message")

log_reader_json = ProfilLoggerReader(handler=json_handler)
# log_reader_csv = ProfilLoggerReader(handler=csv_handler)
# print(log_reader_csv.load_data)
# log_reader_sqlite = ProfilLoggerReader(handler=sql_handler)
# print(log_reader_sqlite.load_data)
# log_reader_txt = ProfilLoggerReader(handler=file_handler)
# print(log_reader_txt.load_data)
# print(log_reader_json.find_by_text("info",'07-07-2021 16:00:00','07-08-2021 22:20:00')) # returns list of LogEntry that contains message: "Some info message"
# print(log_reader_json.find_by_regex(r"\w\w\w\w \w\w\w\w ", '07-07-2021 16:00:00','07-08-2021 22:20:00')) # returns list of logEntry that contains: "Some info message", "Some warning message"
print(log_reader_json.groupby_level('07-01-2021 16:00:00','07-12-2021 22:20:00'))
# print(log_reader_json.groupby_month('07-01-2021 16:00:00','07-12-2021 22:20:00'))