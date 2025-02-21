"""
main prediction script
"""

import os
from pathlib import Path

import pandas as pd

from src.prediction.model import LSTMModel
from src.reading.players import Player

cwd = os.path.dirname(__file__)
csv_path = os.path.join(cwd, "full.csv")
df = pd.read_csv(csv_path, index_col=0)

model = LSTMModel(31, 5, df)
model.build()
model.fit()

directory = Path(cwd=os.path.dirname(__file__))
full_df = pd.DataFrame()
for path in directory.iterdir():
    if path.is_file():
        df = pd.read_csv(path, index_col=0)
        if "total_points" in df.columns:
            try:
                player = Player.from_csv(str(path))
                last_result = player.to_time_steps(5).idxmax()
                to_pred = last_result.drop("total_points")

                print(model.predict(to_pred), last_result["total_points"], player.name)
            except KeyError:
                pass
