from Deep_Classifier.constants import *
from Deep_Classifier.entity import DataIngestionConfig
from Deep_Classifier.utils import read_yaml, create_directories


class Configuration:
    def __init__(self, 
                config_file_path = CONFIG_FILE_PATH,
                parameters_file_path = PARAMETERS_FILE_PATH
                ):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(parameters_file_path)
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config