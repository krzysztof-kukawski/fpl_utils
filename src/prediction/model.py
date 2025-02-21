"""
lstm model module
"""

import pandas as pd
from keras.api.layers import LSTM, Dense
from keras.api.models import Sequential


class LSTMModel:
    """
    lstm time series model

    :param
    """

    def __init__(self, n_vars: int, n_time_steps: int, data: pd.DataFrame):
        self.n_vars = n_vars
        self.n_time_steps = n_time_steps
        self.data = data
        self.model = Sequential()

    def build(self) -> None:
        """

        :return:
        """
        self.model.add(
            LSTM(50, activation="relu", input_shape=(5, 31), return_sequences=True)
        )
        self.model.add(
            LSTM(50, activation="relu", input_shape=(5, 31), return_sequences=True)
        )
        self.model.add(
            LSTM(50, activation="relu", input_shape=(5, 31), return_sequences=True)
        )
        self.model.add(
            LSTM(50, activation="relu", input_shape=(5, 31), return_sequences=True)
        )
        self.model.add(LSTM(50, activation="relu", input_shape=(5, 31)))
        self.model.add(Dense(1))
        self.model.compile(optimizer="adam", loss="relu")

    def fit(self):
        """

        :return:
        """
        x = self.data.drop("total_points", axis=1).to_numpy()
        x = x.reshape(len(x), self.n_time_steps, self.n_vars)
        y = self.data["total_points"].to_numpy()
        self.model.fit(x, y, epochs=100, batch_size=16)

    def predict(self, record: pd.Series):
        """

        :param record:
        :return:
        """
        row = record.to_numpy()
        row = row.reshape(1, self.n_time_steps, self.n_vars)
        return self.model.predict(row)
