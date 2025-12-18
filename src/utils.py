#have all the common things
import os
import sys
import pandas as pd
import dill
from src.exception import CustomException
from src.logger import logger


def save_object(file_path, obj):
    '''
    This function is used to save the object in a file
    '''
    try:
        dir_path= os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        logger.info("Exception occurred while saving object")
        raise CustomException(e, sys)