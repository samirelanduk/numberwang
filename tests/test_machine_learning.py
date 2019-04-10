import random
import numpy as np
import pandas as pd
from unittest import TestCase
import numerus.learning as learning

class Test(TestCase):

    def test_knn(self):
        # Create data
        geodata = pd.read_csv("tests/data/UScounties.csv")
        votedata = pd.read_csv("tests/data/USvote.csv")
        merged = geodata.join(votedata)[:600]
        data = [{
         "input": np.array([row["Longitude"], row["Latitude"]]),
         "output": "GOP" if row["dem_2016"] < row["gop_2016"] else "DEM"
        } for i, row in merged.iterrows()]

        # Create training and testing data
        training_data, test_data = learning.divide_data(data)

        # Train model
        model = learning.KNearestNeighbour(k=1)
        self.assertEqual(model.k, 1)
        self.assertFalse(model.trained)
        model.train(training_data)
        self.assertTrue(model.trained)

        # Test model
        model.test(test_data)
        self.assertGreater(model.accuracy, 0.9)
        self.assertGreater(model.sensitivity("DEM"), 0.74)
        self.assertGreater(model.specificity("DEM"), 0.9)


    def test_perceptron(self):
        # Create data
        irisdata = pd.read_csv("tests/data/iris.csv")
        data = [{
         "input": np.array([row["Sepal length"], row["Petal length"]]),
         "output": 1 if row["Class"] == "Iris-versicolor" else -1
        } for i, row in irisdata.iterrows() if row["Class"] != "Iris-virginica"]

        for Model in (learning.Perceptron, learning.Adaline, learning.StochasticAdaline):
            # Create training and testing data
            training_data, test_data = learning.divide_data(data)

            # Train model
            model = Model(learning_rate=0.1 if Model is learning.Perceptron else 0.0001)
            model.train(training_data)

            # Test model
            model.test(test_data)
            self.assertGreaterEqual(model.accuracy, 0.95)
            self.assertEqual(model.sensitivity(1), 1)
            self.assertEqual(model.specificity(1), 1)
