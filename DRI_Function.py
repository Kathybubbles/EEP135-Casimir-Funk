import pandas as pd

class DRILookup:
  def __init__(self, min_csv: str, max_csv: str):
    self.df_min = pd.read_csv(min_csv)
    self.df_min.set_index("Nutrition", inplace=True)

    self.df_max = pd.read_csv(max_csv)
    self.df_max.set_index("Nutrition", inplace=True)
  
  def get_min_series(self, nutrient: str) -> pd.Series:
    try:
      row = self.df_min.loc[nutrient]
      return row  
    except KeyError:
      return pd.Series(dtype=float)
      
  def get_max_series(self, nutrient: str) -> pd.Series:
    try:
      row = self.df_max.loc[nutrient]
      return row
    except KeyError:
      return pd.Series(dtype=float)