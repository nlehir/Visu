# build a tree for fish
import numpy as np
from sklearn import tree
import graphviz
from sklearn.tree import DecisionTreeClassifier

fish_features = np.load("data/fish_features_blurred.npy")
fish_class = np.load("data/fish_class_blurred.npy")

feature_names = ["length", "weight", "birth hour"]
class_names = ["tuna", "salmon"]

max_depth = 8
classifier = tree.DecisionTreeClassifier(max_depth=max_depth,
                                         criterion="entropy",
                                         min_samples_split=2,
                                         min_samples_leaf=2,
                                         min_impurity_decrease=0.00)
classifier = classifier.fit(fish_features, fish_class)

# convert the graph to graphviz in order to visualize it
dot_data_minimal = tree.export_graphviz(classifier,
                                        out_file=None,
                                        feature_names=feature_names,
                                        class_names=class_names,
                                        filled=True,
                                        rounded=True)
graph = graphviz.Source(dot_data_minimal)
graph.render(f"images/trees/fish_blurred_max_depth_{max_depth}")
