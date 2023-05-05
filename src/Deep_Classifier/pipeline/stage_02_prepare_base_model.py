from Deep_Classifier.config import Configuration
from Deep_Classifier.components import DataIngestion, PrepareBaseModel
from Deep_Classifier import logger

STAGE_NAME = "Prepare Base Model Stage"
def main():
    config = Configuration()
    prepare_base_model_config = config.get_prepare_base_model_config()
    prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
    prepare_base_model.get_base_model()
    prepare_base_model.update_base_model()

if __name__=="__main__":
    try:
        logger.info(f"{'>>'*15} Stage {STAGE_NAME} Started. {'<<'*15}")
        main()
        logger.info(f"{'>>'*15} Stage {STAGE_NAME} Completed. {'<<'*15}")
    except Exception as e:
        logger.exception(e)
        raise e
