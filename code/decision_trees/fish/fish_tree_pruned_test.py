"""
    check test error as a function of the complexity of the tree
"""

from sklearn.model_selection import train_test_split
import numpy as np
from sklearn import tree
import matplotlib.pyplot as plt

fish_features = np.load("data/fish_features_blurred.npy")
fish_class = np.load("data/fish_class_blurred.npy")

feature_names = ["length", "weight", "hour"]
class_names = ["tuna", "salmon"]

X_train, X_test, y_train, y_test = train_test_split(fish_features, fish_class)


def test_depth(max_depth):
    our_tree = tree.DecisionTreeClassifier(max_depth=max_depth,
                                           criterion="entropy")
    # train tree on training arbre
    our_tree = our_tree.fit(X_train, y_train)
    # test tree on test set
    return our_tree.score(X_test, y_test)


scores_on_test_set = list()
max_tested = 15
for depth in range(1, max_tested):
    scores_on_test_set.append(test_depth(depth))

plt.plot(range(1, max_tested), scores_on_test_set)
plt.xlabel("max depth")
plt.ylabel("score on test set")
plt.xticks(range(1, max_tested))
plt.savefig("images/test error function of depth.pdf")
plt.close()


# test min samples leaf
def test_leaf(min_samples_leaf):
    our_tree = tree.DecisionTreeClassifier(min_samples_leaf=min_samples_leaf,
                                           criterion="entropy")
    # train tree on training arbre
    our_tree = our_tree.fit(X_train, y_train)
    # test tree on test set
    return our_tree.score(X_test, y_test)


scores_on_test_set = list()
min_tested = 10
max_tested = 101
tested_min_samples_leaf = np.arange(min_tested, max_tested, 10)
for depth in tested_min_samples_leaf:
    scores_on_test_set.append(test_depth(depth))

plt.plot(tested_min_samples_leaf, scores_on_test_set)
plt.xlabel("min samples leaf")
plt.ylabel("score on test set")
plt.xticks(tested_min_samples_leaf)
plt.savefig("images/test error function of min samples leaf.pdf")
plt.close()
