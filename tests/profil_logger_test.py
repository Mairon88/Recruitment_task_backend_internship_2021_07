import pytest
from scripts import profil_logger
from scripts.handlers import JsonHandler, CSVHandler, SQLLiteHandler, FileHandler

@pytest.fixture
def logger():
    json_handler = JsonHandler("logs.json")
    csv_handler = CSVHandler("logs.csv")
    sql_handler = SQLLiteHandler("logs.sqlite")
    file_handler = FileHandler("logs.txt")

    handlers = [json_handler, csv_handler, sql_handler, file_handler]

    logger = profil_logger.ProfilLogger(handlers)

    return logger

def test_profil_logger_init(logger):
    assert logger

def test_profil_logger_info(logger):
    assert logger.info('Some info message') == 'Some info message'

def test_profil_logger_warning(logger):
    assert logger.warning('Some warning message') == 'Some warning message'

def test_profil_logger_debug(logger):
    assert logger.debug('Some debug message') == 'Some debug message'

def test_profil_logger_critical(logger):
    assert logger.critical('Some critical message') == 'Some critical message'

def test_profil_logger_error(logger):
    assert logger.error('Some error message') == 'Some error message'

def test_profil_logger_set_log_level(logger):
    assert logger.set_log_level('info') == 'INFO'




