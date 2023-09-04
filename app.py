from src.data_science_project.logger import logging
from src.data_science_project.exception import CustomException
from src.data_science_project.components.data_ingestion import DataIngestion
from src.data_science_project.components.data_ingestion import DataIngestionConfig
import sys


if __name__ == '__main__':
    logging.info("The execution has been completed")

    try:
        #data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)

