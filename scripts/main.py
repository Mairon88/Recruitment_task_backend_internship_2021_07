from handlers import JsonHandler, CSVHandler, SQLLiteHandler, FileHandler
from profil_logger import ProfilLogger

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

