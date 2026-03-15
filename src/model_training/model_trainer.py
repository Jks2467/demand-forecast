from data_loader.data_preprocess import DataPreProcess
from sklearn.multioutput import MultiOutputRegressor
import xgboost as xgb
import joblib
from config.config_loader import ConfigLoader
import pandas as pd

model_path = ConfigLoader().load_config()['artifacts']['model']
data_path = ConfigLoader().load_config()['artifacts']['processed_dataset']


class ModelTrain():
    def __init__(self):
        self.model_path = model_path
        self.data_path = data_path

    def process_data_for_model(self):
        self.data_obj = DataPreProcess()
        self.data = self.data_obj.save_dataset()

    def train(self):
        df = pd.read_csv(data_path)
        df = df.set_index('order_date')
        df.index = pd.to_datetime(df.index)

        y_cols = [yc for yc in df.columns if "y_t" in yc]
        x_cols = [xc for xc in df.columns if xc not in y_cols]

        X = df[x_cols]
        y = df[y_cols]

        # train test split
        trains_size = 0.8
        train_idx = int(len(X) * trains_size)

        X_train = X[:train_idx]
        X_test = X[train_idx:]
        y_train = y[:train_idx]
        y_test = y[train_idx:]

        best_params = {'n_estimators': 1200,
             'learning_rate': 0.008733861473432712,
             'max_depth': 12,
             'gamma': 0.19391770188922408,
             'colsample_bytree': 0.9249588586944499,
             'colsample_bylevel': 0.6941421463420491,
             'colsample_bynode': 0.7340866896134831,
             'reg_alpha': 0.1688427635766734,
             'reg_lambda': 3.076245449543594e-05,
             'max_delta_step': 5,
             'max_bin': 256}
        
        base_model = xgb.XGBRegressor(**best_params)

        model = MultiOutputRegressor(base_model)

        model.fit(
            X_train,
            y_train,
            verbose=True
        )

        return model
    
    def save_model(self):
        self.model = self.train()
        joblib.dump(self.model, model_path)
        return self.model
    

model = ModelTrain().save_model()