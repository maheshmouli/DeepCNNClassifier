from Deep_Classifier.config import Configuration
from Deep_Classifier.components import PrepareCallback, Training
from Deep_Classifier import logger

STAGE_NAME = "Prepare Call-Back & Training Stage"
def main():
    config = Configuration()
    prepare_callbacks_config = config.get_prepare_callback_config()
    prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
    callback_list = prepare_callbacks.get_tensorboard_checkpoint_callbacks()

    training_config = config.get_training_config()
    training = Training(config=training_config)
    training.get_base_model()
    training.train_valid_generator()
    training.train(callback_list = callback_list)

if __name__=="__main__":
    try:
        logger.info(f"{'>>'*15} Stage {STAGE_NAME} Started. {'<<'*15}")
        main()
        logger.info(f"{'>>'*15} Stage {STAGE_NAME} Completed. {'<<'*15}")
    except Exception as e:
        logger.exception(e)
        raise e
