import os
from pathlib import Path
import logging

# print(Path("A\B\c.txt")) --  why we Path

list_of_files=[
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipleline/__init__.py",
    "src/pipleline/training_pipeline.py",
    "src/pipleline/prediction_pipeline.py",
    "src/utils/__init__.py"
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception.py",
    "test/unit/__init__.py",
    "test/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info((f"Creating Directory: {filedir} for file: {filename}"))

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file