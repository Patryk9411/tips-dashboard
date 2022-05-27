import pandas as pd
import seaborn as sb


def tips_df() -> pd.DataFrame:
    return sb.load_dataset("tips")
