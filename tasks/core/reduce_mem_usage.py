"""Module for functions that optimize the used memory for data storage."""

import pandas as pd
import numpy as np


def reduce_mem_usage(df: pd.DataFrame) -> pd.DataFrame:
    """Convert the data type to a more economical one

    :param df: original date frame
    :type df: pd.DataFrame
    :return: the same date frame, with corrected data types
    :rtype: pd.DataFrame
    """

    start_mem = df.memory_usage().sum()/1024**2
    for col in df.columns:
        col_type = df[col].dtypes

        if str(col_type)[:5] == "float":
            c_min = df[col].min()
            c_max = df[col].max()

            if c_min > np.finfo("f2").min and c_max < np.finfo("f2").max:
                df[col] = df[col].astype(np.float16)
            elif c_min > np.finfo("f4").min and c_max < np.finfo("f4").max:
                df[col] = df[col].astype(np.float32)
            else:
                df[col] = df[col].astype(np.float64)

        elif str(col_type)[:3] == "int":
            c_min = df[col].min()
            c_max = df[col].max()

            if c_min > np.iinfo("i1").min and c_max < np.iinfo("i1").max:
                df[col] = df[col].astype(np.int8)
            elif c_min > np.iinfo("i2").min and c_max < np.iinfo("i2").max:
                df[col] = df[col].astype(np.int16)
            elif c_min > np.iinfo("i4").min and c_max < np.iinfo("i4").max:
                df[col] = df[col].astype(np.int32)
            elif c_min > np.iinfo("i8").min and c_max < np.iinfo("i8").max:
                df[col] = df[col].astype(np.int64)

        elif col == "timestamp":
            df[col] = pd.to_datetime(df[col])

        elif str(col_type)[:8] != "datetime":
            df[col] = df[col].astype("category")

    end_mem = df.memory_usage().sum() / 1024**2
    print(
        f"Потребление памяти меньше на - {round(start_mem - end_mem, 2)} Мб (минус {round(100*(start_mem - end_mem)/start_mem, 1)}%)")
    return df
