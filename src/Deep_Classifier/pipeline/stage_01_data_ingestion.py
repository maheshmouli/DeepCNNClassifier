from Deep_Classifier.config import Configuration
from Deep_Classifier.components import DataIngestion
from Deep_Classifier import logger

STAGE_NAME = "Data Ingestion Stage"
def main():
    config = Configuration()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.unzip_and_clean()

if __name__=="__main__":
    try:
        logger.info(f"{'>>'*15} Stage {STAGE_NAME} Started. {'<<'*15}")
        main()
        logger.info(f"{'>>'*15} Stage {STAGE_NAME} Completed. {'<<'*15}")
    except Exception as e:
        logger.exception(e)
        raise e
