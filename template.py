import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s: ')

PACKAGE_NAME = "Deep_Classifier"

LIST_OF_FILES = [
    ".github/workflows/.gitkeep",
    f"src/{PACKAGE_NAME}/__init__.py"
    f"src/{PACKAGE_NAME}/components/__init__.py",
    f"src/{PACKAGE_NAME}/utils/__init__.py",
    f"src/{PACKAGE_NAME}/config/__init__.py",
    f"src/{PACKAGE_NAME}/pipeline/__init__.py",
    f"src/{PACKAGE_NAME}/entity/__init__.py",
    f"src/{PACKAGE_NAME}/constants/__init__.py",
    "configs/config.yaml",
    "data_version_control.yaml",
    "parameters.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "research/trails.ipynb",
    "example."
]

for filepath in list(LIST_OF_FILES):
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory: {filedir} for file: {filename}.")

    # Creating an empty file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass 
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists.")
