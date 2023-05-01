import os
import urllib.request as request
from zipfile import ZipFile
from Deep_Classifier.entity import DataIngestionConfig
from Deep_Classifier import logger
from Deep_Classifier.utils import get_size
from pathlib import Path
from tqdm import tqdm

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        logger.info("Downloading the File...")
        if not os.path.exists(self.config.local_data_file):
            logger.info("Downloading Started...")
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename= self.config.local_data_file
            )
            logger.info(f"{filename} Downloaded with following info: \n{headers}")
        else:
            logger.info(f"File Already Exists of size: {get_size(Path(self.config.local_data_file))}")
            
    def _get_updated_list_of_files(self, list_of_files):
        return [f for f in list_of_files if f.endswith(".jpg") and ("Cat" in f or "Dog" in f)]

    def _preprocess(self, zfile: ZipFile, f: str, working_dir: str):
        target_filepath = os.path.join(working_dir, f)
        if not os.path.exists(target_filepath):
            zfile.extract(f, working_dir)

        if os.path.getsize(target_filepath) == 0:
            os.remove(target_filepath)
            logger.info(f"Removing File:{target_filepath}")

    def unzip_and_clean(self):
        logger.info(f"Unzipping the File aand removing unwanted files")
        with ZipFile(file=self.config.local_data_file, mode="r") as zfile:
            list_of_files = zfile.namelist()
            updated_list_of_files = self._get_updated_list_of_files(list_of_files)
            # print(updated_list_of_files)
            for f in tqdm(updated_list_of_files):
                self._preprocess(zfile, f, self.config.unzip_dir)
