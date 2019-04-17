import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from collections import Counter

def display_dataset(dataframe, title="", show=True):
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


def divide_data(data, test=0.2):
    data = data.sample(frac=1)
    test_cutoff = int(test * len(data))
    return data[:-test_cutoff], data[test_cutoff:]



class Model:
    """A model is something which predicts. That is, it takes in some input
    vector representing one or more features and, once it has been trained in
    some way, maps the input to a predicted category (in the case of
    classification) or value (in the case of regression)."""

    def __init__(self, training_data):
        self.training_data = training_data
        self.training_inputs = training_data.iloc[:, 0:2].values
        self.training_outputs = training_data.iloc[:, 2:3].values
        self.trained = False
        self.dimensions = len(self.training_inputs[0])
        self.test_data = []


    def __call__(self, input):
        return np.array([np.random.choice([-1, 1]) for _ in input])


    def display(self):

        x1_min = self.training_inputs[:, 0].min() - 1
        x1_max = self.training_inputs[:, 0].max() + 1
        x2_min = self.training_inputs[:, 1].min() - 1
        x2_max = self.training_inputs[:, 1].max() + 1
        colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
        cmap = ListedColormap(colors[:len(np.unique(self.training_outputs))])
        xx1, xx2 = np.meshgrid(
         np.arange(x1_min, x1_max, 0.02), np.arange(x2_min, x2_max, 0.02)
        )
        Z = self(np.array([xx1.ravel(), xx2.ravel()]).T)
        Z = Z.reshape(xx1.shape)
        plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
        display_dataset(self.training_data)
        plt.show()




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

    '''def __init__(self, *args, learning_rate=0.01, epochs=100, **kwargs):
        super().__init__(*args, **kwargs)
        self.weights = np.array([0.5 for _ in range(self.dimensions)])
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.threshold = 0


    def __repr__(self):
        return f"<Perceptron ({self.dimensions} dimensions, {'' if self.trained else 'un'}trained, learning_rate={self.learning_rate}, epochs={self.epochs}, weights={self.weights}, threshold={self.threshold})>"


    def __call__(self, input):
        # What is the combined effect of all the input features?
        z = self.process_input(input)

        # Is this enough to fire?
        return 1 if z > self.threshold else -1


    def process_input(self, input):
        """Takes an input vector and determines the net outcome based on the
        perceptron's weights."""

        return input.dot(self.weights)


    def train(self, training_data):
        # Create weight vector of the appropriate number of dimensions
        dimension_count = len(training_data[0]["input"])
        self.weights = np.array([0.5 for _ in range(dimension_count)])

        # Pass through the training data a predetermined number of times, and
        # track how long it takes to converge
        self.convergence = []
        for n in range(self.epochs):
            # Track how many errors are in this pass through
            errors = 0

            # Go through every object in the training data
            for input in training_data:
                # Get the actual input vector
                input_vector = np.array(input["input"][:])

                # What does the perceptron currently map this input to?
                predicted_output = self(input_vector)

                # What should it be mapping it to?
                correct_output = input["output"]

                # Update errors if this is wrong
                errors += int(correct_output != predicted_output)

                # Update the weights vector
                input_vector = np.insert(input_vector, 0, 1)
                delta = self.learning_rate * (correct_output - predicted_output)
                self.threshold += delta
                for dimension in range(len(self.weights)):
                    self.weights[dimension] += (input_vector[dimension] * delta)

            # Update convergence data
            self.convergence.append((n, errors))

        # The model has now been trained
        self.trained = True



class Adaline(Perceptron):

    def __call__(self, input):
        # What is the combined effect of all the inputs?
        z = self.process_input(input)

        # Activate the net input
        activated_z = self.activate(z)

        # Is this enough to fire?
        return 1 if z > self.threshold else -1


    def activate(self, z):
        return z


    def train(self, training_data):
        # Create weight vector of the appropriate number of dimensions
        dimension_count = len(training_data[0]["input"])
        self.weights = np.array([0.5 for _ in range(dimension_count)])

        # Get the inputs as a matrix
        inputs = np.array([input["input"] for input in training_data])

        # Get the correct outputs as a vector
        correct_outputs = np.array([input["output"] for input in training_data])

        # Pass through the training data a predetermined number of times, and
        # track how long it takes to converge
        self.convergence = []
        for n in range(self.epochs):

            # What are the neuron activations for all the inputs
            activations = self.process_input(inputs)

            # What is the sum of squared error of this performance?
            errors = correct_outputs - activations
            sum_error_squared = (errors ** 2).sum() / 2

            # What should the new threshold be?
            self.threshold += self.learning_rate * errors.sum()

            # What should the new weights be?
            self.weights += self.learning_rate * inputs.T.dot(errors)

            # Update convergence
            self.convergence.append((n, sum_error_squared))

        # The model has now been trained
        self.trained = True



class StochasticAdaline(Adaline):

    def train(self, training_data):
        # Create weight vector of the appropriate number of dimensions
        dimension_count = len(training_data[0]["input"])
        self.weights = np.array([0.5 for _ in range(dimension_count)])

        # The model has now been trained
        self.trained = True

        # Get the inputs as a matrix
        inputs = np.array([input["input"] for input in training_data])

        # Get the correct outputs as a vector
        correct_outputs = np.array([input["output"] for input in training_data])

        # Pass through the training data a predetermined number of times, and
        # track how long it takes to converge
        self.convergence = []
        for n in range(self.epochs):
            # Get a shuffled copy of the inputs
            matrix_indices = np.random.RandomState().permutation(len(inputs))
            shuffled_inputs = inputs[matrix_indices]

            # Shuffle the outputs so that they match the shuffled inputs
            shuffled_correct_outputs = correct_outputs[matrix_indices]

            # Go through every input and its output
            costs = []
            for input, correct_output in zip(shuffled_inputs,  shuffled_correct_outputs):
                # What is the activation for this output?
                activation = self.activate(self.process_input(input))

                # How far off is this?
                error = correct_output - activation

                # Update the threshold
                self.threshold += self.learning_rate * error

                # Update the weights
                self.weights += self.learning_rate * input.dot(error)

                # How far off was the neuron?
                costs.append(0.5 * error ** 2)

            # How did the neuron perform over all inputs?
            average_cost = sum(costs) / len(costs)
            self.convergence.append((n, average_cost))'''
