import pandas as pd

class DRILookup:
    """
    A helper class to retrieve Dietary Reference Intake (DRI) values
    from diet_minimums.csv and diet_maximums.csv.

    Usage:
        dri = DRILookup("diet_minimums.csv", "diet_maximums.csv")
        min_val = dri.get_min("Protein", "F 19-30")
        max_val = dri.get_max("Sodium, Na", "F 19-30")
    """

    def __init__(self, min_csv: str, max_csv: str):
        """
        :param min_csv: path to diet_minimums.csv
        :param max_csv: path to diet_maximums.csv

        We do NOT drop 'Unnamed: 0', so that column remains in the DataFrame.
        """
        # 1) Read diet_minimums
        self.df_min = pd.read_csv(min_csv)
        # Just set "Nutrition" as index.
        self.df_min.set_index("Nutrition", inplace=True)

        # 2) Read diet_maximums
        self.df_max = pd.read_csv(max_csv)
        self.df_max.set_index("Nutrition", inplace=True)

    def get_min(self, nutrient: str, group: str) -> float:
        """
        Return the minimum recommended intake (RDA/AI) for a given nutrient & group
        (e.g. 'F 19-30'). If not found or invalid, return None.
        """
        try:
            val = self.df_min.loc[nutrient, group]
            return float(val)
        except (KeyError, ValueError):
            return None

    def get_max(self, nutrient: str, group: str) -> float:
        """
        Return the maximum tolerable intake (UL) for a given nutrient & group
        (e.g. 'F 19-30'). If not found or invalid, return None.
        """
        try:
            val = self.df_max.loc[nutrient, group]
            return float(val)
        except (KeyError, ValueError):
            return None