print("\n----------------------------------------------------\nExercise 1:")
def classify(input_tuple):
    """Classify people's health status by comparing their age,
    smoking habits and diet."""
    smoker, age, diet = input_tuple
    if smoker == 'yes':
        if int(age) <  29.5:
            return 'less'
        else:
            return 'more'
    else:
        if diet == 'good':
            return 'less'
        else:
            return 'more'

test = classify(('yes', 31, 'good'))
assert test == 'more'
print(test)

print("\n----------------------------------------------------\nExercise 2:")

file_test = 'health-test.txt'
health_test = []

with open(file_test, 'r') as con:
    for line in con:
        extention = line.strip().split(',')
        health_test.append(tuple(extention))
print(health_test)
print("\n----------------------------------------------------\nExercise 3:")

health_tree = []
for subject in health_test:
    health_tree.append(classify(subject))

more_perc = float(health_tree.count('more')) / len(health_tree)
print("predictions: %s" % health_tree)
print("percentage of 'more': %s" % more_perc)

print("\n----------------------------------------------------\nExercise 4:")

file_train = 'health-train.txt'
health_train = []
with open(file_train) as con:
    for line in con:
        content = line.strip().split(',')
        health_train.append((tuple(content[:3]), content[-1]))

print("train-set:\n", health_train)
print("\n----------------------------------------------------\nExercise 5:")
def d(a, b):
    """Calculate distance metric."""
    return (a[0]!=b[0]) + ((float(a[1])-float(b[1]))/50)**2 + (a[2]!=b[2])

def get_nearest_neighbor(target, train_set):
    dist = [d(target, x[0]) for x in train_set]
    return train_set[dist.index(min(dist))]

neighborino = get_nearest_neighbor(('yes', 31, 'good'), health_train)
print(neighborino)

health_neighbor = []

for subject in health_test:
    extention = get_nearest_neighbor(subject, health_train)
    health_neighbor.append(extention[1])

print("Predictions by Decision Tree:\n%s" % health_tree)
print("Predictions by Nearest Neighbor Algorithm:\n%s" % health_neighbor)

indices = []
different = []

for i in range(len(health_tree)):
    if health_tree[i] != health_neighbor[i]:
        indices.append(i)
        different.append(health_test[i])

difference_prob = float(len(different)) / len(health_tree)

print("Index: %s\nDatapoint: %s" % (indices, different))
print("Probability: %s" % difference_prob)
# stay consistent with problem sheet.
print((different, difference_prob))

print("\n----------------------------------------------------\nExercise 6:")

class NearestMeanClassifier(object):
    """Training Method that takes a dataset as input and produces two internal
    vectors corresponding to the mean of each class."""
    def __init__(self):
        classes = []
        for line in dataset:
            if line[1] not in classes:
                classes.append(line[1])
        self.classes = classes
    def train(self, dataset):
        for classes in self.classes:
