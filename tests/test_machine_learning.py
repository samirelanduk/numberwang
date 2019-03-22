import random
import pandas as pd
from unittest import TestCase
import numerus.learning as learning

class Test(TestCase):

    def test(self):
        # Create data
        geodata = pd.read_csv("tests/data/UScounties.csv")
        votedata = pd.read_csv("tests/data/USvote.csv")
        merged = geodata.join(votedata)[:1000]
        data = [{
         "input": [row["Longitude"], row["Latitude"]],
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
        self.assertGreater(model.sensitivity("DEM"), 0.75)
        self.assertGreater(model.specificity("DEM"), 0.9)
