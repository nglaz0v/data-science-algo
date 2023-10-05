"""Module for functions that show graphs."""


import matplotlib.pyplot as plt

from typing import List
from pandas import DataFrame
from numpy import ceil

def data_correlation_plot(df: DataFrame, columns: List[str], y_column: str):
    """Show set of scatter plots

    :param df: dataframe with data to display on a chart
    :type df: DataFrame
    :param columns: dataframe columns that will be displayed on the x-axis
    :type columns: List[str]
    :param y_column: dataframe column that will be displayed on the y-axis
    :type y_column: str
    """

    rows = int(ceil(len(columns) / 4))
    fig = plt.figure(figsize=(12, rows*3))
    for i, column in enumerate(columns):
        type_ = str(df[column].dtypes)
        if type_[:3] == "int" or type_[:5] == "float":
            area = fig.add_subplot(rows, 4, i+1)
            DataFrame(
                df,
                columns=[y_column, column]
            ).plot.scatter(
                x=column,
                y=y_column,
                ax=area
            )
    plt.tight_layout()
    plt.show()