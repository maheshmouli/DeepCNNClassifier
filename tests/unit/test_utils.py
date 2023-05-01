import pytest
from Deep_Classifier.utils import read_yaml
from pathlib import Path
from box import ConfigBox

yaml_files = [
    "tests/data/empty.yaml",
    "tests/data/demo.yaml"
]

def test_read_yaml_empty():
    with pytest.raises(ValueError):
        read_yaml(Path(yaml_files[0]))

