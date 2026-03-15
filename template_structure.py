import os
from pathlib import Path # For handling file paths robustly
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

project_name = 'src'

dir_list = [
    ".github/workflows/.gitkeep",
    "config.yaml",
    "setup.py",
    "app.py",
    f"{project_name}/__init__.py",
    f"{project_name}/model_training/__init__.py",
    f"{project_name}/data_loader/__init__.py",
    f"{project_name}/prediction/__init__.py",
    f"{project_name}/model_training/model_trainer.py",
    f"{project_name}/data_loader/data_loader.py",
    f"{project_name}/prediction/predictor.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/config/config_loader.py",
    f"artifacts/trained_model",
]


for item in dir_list:
    path = Path(item)
    
    if path.suffix:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch()
        logging.info(f"created file path {path}")
    else:
        path.mkdir(parents=True, exist_ok=True)
        logging.info(f"created directory path {path}")

print("Structure created.")