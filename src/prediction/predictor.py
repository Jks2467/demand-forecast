from config.config_loader import ConfigLoader
import joblib
import xgboost as xgb
import pandas as pd

load_model_path = ConfigLoader().load_config()['artifacts']['load_model']

class Predict():
    def __init__(self):
        self.path = load_model_path

    def predict(self, df: pd.DataFrame):
        model = joblib.load(self.path)
        return model.predict(df)