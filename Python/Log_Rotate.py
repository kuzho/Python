from logging import getLogger, Formatter, INFO
from logging.handlers import RotatingFileHandler
#------------------------------------------------------------------------------#
def Log_Rotate():
    try:
        logger = getLogger('Log_Rotate')
        logger.setLevel(INFO)
        formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler = RotatingFileHandler('Log_Rotate.log', maxBytes=100*5, backupCount=3)
        file_handler.setLevel(INFO)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.info(f'Log_Rotate.py is running')
    except Exception as e:
        logger.error(f'Error: {e}')
#------------------------------------------------------------------------------#
if __name__ == '__main__':
    Log_Rotate()