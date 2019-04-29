import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from collections import Counter

def plot_dataset(dataframe, title="", show=True):
    column_names = dataframe.columns
    for label in np.unique(dataframe[column_names[2]]):
        df = dataframe[dataframe[column_names[2]] == label]
        plt.scatter(df[column_names[0]], df[column_names[1]], label=label)
    plt.xlabel(column_names[0])
    plt.ylabel(column_names[1])
    plt.title(title)
    plt.legend()
    if show:
        plt.show()
