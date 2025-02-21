"""
time steps
"""

from warnings import simplefilter

import pandas as pd
from numpy import ndarray
from pandas.errors import PerformanceWarning

simplefilter("ignore", PerformanceWarning)


class TimeStepsTransformer:
    """
    Transforms data into time step sequence
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.vars = list(df.columns)

    def transform(self, n_time_steps: int) -> pd.DataFrame:
        """

        :param n_time_steps:
        :return:
        """
        transformed_df = self.df.copy()
        transformed_df.drop(["name", "id"], axis=1, inplace=True)
        self.vars.remove("name")
        self.vars.remove("id")
        for time_step in range(n_time_steps, 0, -1):
            for var in self.vars:
                transformed_df[f"{var} - {time_step}"] = self.df[var].shift(time_step)

        self.vars.remove("total_points")
        print("removed!")
        transformed_df.drop(self.vars, axis=1, inplace=True)
        transformed_df.dropna(inplace=True)
        return transformed_df

    def to_numpy(self, n_time_steps: int) -> tuple[ndarray, ndarray]:
        """

        :param n_time_steps:
        :return:
        """
        df = self.transform(n_time_steps)
        features = df.drop("total_points").to_numpy()
        target = df["total_points"].to_numpy()

        return features, target
