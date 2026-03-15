from config.config_loader import ConfigLoader
import pandas as pd

class DataLoader():
    def __init__(self):
        self.config = ConfigLoader().load_config()
    
    def load_data(self):
        self.file_path = self.config['artifacts']['dataset']
        file_frame = pd.read_csv(self.file_path)
        return file_frame
