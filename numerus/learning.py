import random
import numpy as np
from collections import Counter

def divide_data(data, test=0.2):
    data = data[:]
    random.shuffle(data)
    test_cutoff = int(test * len(data))
    return data[:-test_cutoff], data[test_cutoff:]



class Model:
    """A model is something which predicts. That is, it takes in some input
    vector representing one or more features and, once it has been trained in
    some way, maps the input to a predicted category (in the case of
    classification) or value (in the case of regression)."""

    def __init__(self):
        self.trained = False
        self.training_data = []
        self.test_data = []


    def test(self, data):
        self.test_data = data
        for obj in data:
            prediction = self(obj["input"])
            obj["correct"] = prediction == obj["output"]


    @property
    def accuracy(self):
        return len([o for o in self.test_data if o["correct"]]) / len(self.test_data)


    def true_positives(self, output):
        return len([o for o in self.test_data if o["correct"] and o["output"] == output])


    def true_negatives(self, output):
        return len([o for o in self.test_data if o["correct"] and o["output"] != output])


    def false_positives(self, output):
        return len([o for o in self.test_data if not o["correct"] and o["output"] != output])


    def false_negatives(self, output):
        return len([o for o in self.test_data if not o["correct"] and o["output"] == output])


    def confusion_matrix(self, output):
        return np.array([[self.true_positives(output), self.false_positives(output)], [self.true_negatives(output), self.false_negatives(output)]])


    def sensitivity(self, output):
        return self.true_positives(output) / (self.true_positives(output) + self.false_negatives(output))


    def specificity(self, output):
        return self.true_negatives(output) / (self.true_negatives(output) + self.false_positives(output))



class KNearestNeighbour(Model):

    def __init__(self, k):
        Model.__init__(self)
        self.k = k


    def __call__(self, input):
        ordered_data = []
        for obj in self.training_data:
            distance = sum([(a - b) ** 2 for a, b in zip(obj["input"], input)]) ** 0.5
            ordered_data.append([obj["output"], distance])
        ordered_data.sort(key=lambda d: d[1])
        neighbors = ordered_data[:self.k]
        common = Counter([n[0] for n in neighbors])
        return common.most_common(1)[0][0]


    def train(self, data):
        self.training_data = data
        self.trained = True



class Perceptron(Model):

    def __init__(self):
        self.learning_rate = 0.1
        self.epochs = 50


    def __call__(self, input):
        # Add 1 to the beginning to account for the threshold input.
        input = np.array([1] + input)

        # What is the combined effect of all the inputs?
        z = input.dot(self.weights)

        # Is this enough to fire?
        return 1 if z > 0 else -1


    def train(self, training_data):
        # Create weight vector of the appropriate number of dimensions
        dimension_count = len(training_data[0]["input"])
        self.weights = np.array([0.5 for _ in range(dimension_count + 1)])

        # Pass through the training data a predetermined number of times, and
        # track how long it takes to converge
        self.convergence = []
        for n in range(self.epochs):
            # Track how many errors are in this pass through
            errors = 0

            # Go through every object in the training data
            for input in training_data:
                # Get the actual input vector
                input_vector = input["input"][:]

                # What does the perceptron currently map this input to?
                predicted_output = self(input_vector)

                # What should it be mapping it to?
                correct_output = input["output"]

                # Update errors if this is wrong
                errors += int(correct_output != predicted_output)

                # Update the weights vector
                input_vector.insert(0, 1)
                delta = self.learning_rate * (correct_output - predicted_output)
                self.weights[0] += delta
                for dimension in range(1, len(self.weights)):
                    self.weights[dimension] += (input_vector[dimension] * delta)

            # Update convergence data
            self.convergence.append((n, errors))

        # The model has now been trained
        self.trained = True
