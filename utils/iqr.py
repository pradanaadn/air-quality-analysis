from typing import Tuple, Annotated
import pandas as pd
import numpy as np


def iqr_outlier_threshold(
    df_series: pd.Series,
) -> Annotated[Tuple[float, float], "(Lower bound, Upper bound)"]:
    q1 = df_series.quantile(0.25)
    q3 = df_series.quantile(0.75)
    IQR = q3 - q1
    print(f"Q1 : {q1}\nQ3 : {q3}\nIQR : {IQR}")
    lower_bound = q1 - 1.5 * IQR
    upper_bound = q3 + 1.5 * IQR

    return lower_bound, upper_bound


def get_outlier_index(
    df_series: pd.Series,
) -> Annotated[
    Tuple[np.ndarray, np.ndarray], "(Lower outlier array, Upper outlier array)"
    
]:
    threshold_lower, threshold_upper = iqr_outlier_threshold(df_series)
    lower_outlier_array = np.where(df_series <= threshold_lower)[0]
    upper_outlier_array = np.where(df_series >= threshold_upper)[0]
    
    return lower_outlier_array, upper_outlier_array


    
