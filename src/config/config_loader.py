import yaml
from pathlib import Path
import os

config_path = os.path.join(Path.cwd(), 'config.yaml')

class ConfigLoader():
    def __init__(self):
        self.config_path=config_path
    
    def load_config(self):
        with open(self.config_path, 'r') as f:
            config = yaml.safe_load(f)
        return config
    

# tr_c = ConfigLoader()
# print(tr_c.load_config()['artifacts']['model'])
