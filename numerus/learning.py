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


def split_data(df, test=0.2):
    data = df.sample(frac=1)
    test_cutoff = int(test * len(data))
    return data.iloc[:-test_cutoff], data.iloc[test_cutoff:]



class Model:

    def __init__(self, training_data):
        self.training_data = training_data
        self.input_matrix = training_data.iloc[:,:-1].values
        self.output_vector = training_data.iloc[:,-1:].values[:, 0]
        hot = self.output_vector[0]
        self.output_vector[self.output_vector == hot] = 1
        self.output_vector[self.output_vector != 1] = -1
        self.dimension = len(self.input_matrix[0])



class Perceptron(Model):

    def __init__(self, *args, **kwargs):
        super(Perceptron, self).__init__(*args, **kwargs)
        self.threshold = 0
        self.weights = np.array([1 for _ in range(self.dimension)])


    def __repr__(self):
        return "<{}-dimensional Perceptron ({}-{})>".format(
         self.dimension,
         self.threshold,
         ",".join(map(str, self.weights))
        )
