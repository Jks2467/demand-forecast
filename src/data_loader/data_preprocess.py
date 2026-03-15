from data_loader.data_loader import DataLoader
import pandas as pd
from config.config_loader import ConfigLoader

save_path = ConfigLoader().load_config()['artifacts']['processed_dataset']


class DataPreProcess():
    def __init__(self):
        self.raw = DataLoader().load_data()

    def preprocess(self) -> pd.DataFrame:

        df = self.raw[['order_date', 'shipment_id']]

        df = df.pivot_table(index='order_date', values='shipment_id', aggfunc='sum')

        # df.set_index('order_date', inplace=True)

        df = df.sort_index()

        df.index = pd.to_datetime(df.index)

        df['month'] = df.index.month
        df['weeknum'] = df.index.isocalendar().week
        df['quarter'] = df.index.quarter
        print('features created - month, week, quarter')


        lag_days = [1,2,3,7,14,28]
        for lag in lag_days:
            df[f"lag_{lag}"] = df['shipment_id'].shift(lag)
        print(f'lags created - {lag_days}')


        horizon = 30
        for h in range(1, horizon+1):
            df[f"y_t+{h}"] = df["shipment_id"].shift(-h)
        print(f'Horizon created - {horizon}')

        df.dropna(axis=0, inplace=True)

        return df
    
    def save_dataset(self):
        self.processed_dataset = self.preprocess()
        self.processed_dataset.to_csv(save_path)
        return print(save_path)