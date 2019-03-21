import random
from collections import Counter

def divide_data(data, test=0.2):
    data = data[:]
    random.shuffle(data)
    test_cutoff = int(test * len(data))
    return data[:-test_cutoff], data[test_cutoff:]




class KNearestNeighbour:

    def __init__(self, k):
        self._k = k
        self._trained = False
        self._training_data = []
        self._test_data = []


    def __call__(self, input):
        ordered_data = []
        for obj in self._training_data:
            distance = sum([(a - b) ** 2 for a, b in zip(obj["input"], input)]) ** 0.5
            ordered_data.append([obj["output"], distance])
        ordered_data.sort(key=lambda d: d[1])
        neighbors = ordered_data[:self.k]
        common = Counter([n[0] for n in neighbors])
        return common.most_common(1)[0][0]


    @property
    def k(self):
        return self._k


    @property
    def trained(self):
        return self._trained


    def train(self, data):
        self._training_data = data
        self._trained = True


    def test(self, data):
        self._test_data = data
        for obj in data:
            prediction = self(obj["input"])
            obj["correct"] = prediction == obj["output"]


    @property
    def accuracy(self):
        return len([o for o in self._test_data if o["correct"]]) / len(self._test_data)


    def true_positives(self, output):
        return len([o for o in self._test_data if o["correct"] and o["output"] == output])


    def true_negatives(self, output):
        return len([o for o in self._test_data if o["correct"] and o["output"] != output])


    def false_positives(self, output):
        return len([o for o in self._test_data if not o["correct"] and o["output"] != output])


    def false_negatives(self, output):
        return len([o for o in self._test_data if not o["correct"] and o["output"] == output])


    def sensitivity(self, output):
        return self.true_positives(output) / (self.true_positives(output) + self.false_negatives(output))


    def specificity(self, output):
        return self.true_negatives(output) / (self.true_negatives(output) + self.false_positives(output))
