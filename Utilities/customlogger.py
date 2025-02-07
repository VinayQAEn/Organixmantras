import logging
import inspect
class customlogger:
    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        File_handler = logging.FileHandler("/Users/riyabakoria/OrganixmantraAPP/Logs/logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")  
        File_handler.setFormatter(formatter)
        logger.addHandler(File_handler)
        logger.setLevel(logging.DEBUG)
        return logger
