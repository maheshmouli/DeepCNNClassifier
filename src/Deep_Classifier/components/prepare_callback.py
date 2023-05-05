import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from Deep_Classifier.entity import PrepareCallbacksConfig
import time

class PrepareCallback:
    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config

    @property
    def _create_tensorboard_callbacks(self):
        time_stamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tensorboard_running_logdir = os.path.join(
            self.config.tensorboard_root_log_dir,
            f"tensorboard_logs_at{time_stamp}",
        )
        return tf.keras.callbacks.TensorBoard(log_dir=tensorboard_running_logdir)
    
    @property
    def _create_checkpoint_callbacks(self):

        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath,
            save_best_only=True
        )
    
    def get_tensorboard_checkpoint_callbacks(self):
        return [
            self._create_tensorboard_callbacks,
            self._create_checkpoint_callbacks
        ]