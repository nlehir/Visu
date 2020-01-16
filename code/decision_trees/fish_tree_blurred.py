# build a tree for fish
import numpy as np
import ipdb
from sklearn import tree
import graphviz
from sklearn.tree import DecisionTreeClassifier

fish_features = np.load("fish_features_blurred.npy")
fish_class = np.load("fish_class_blurred.npy")

feature_names = ["length", "weight"]
class_names = ["tuna", "salmon"]

max_depth = 2
our_tree = tree.DecisionTreeClassifier(max_depth=max_depth,
                                       criterion="entropy",
                                       min_samples_split=0,
                                      min_impurity_decrease=0.0)
our_tree = our_tree.fit(fish_features, fish_class)

# convert the graph to graphviz in order to visualize it
dot_data_minimal = tree.export_graphviz(our_tree,
                                        out_file=None,
                                        feature_names=feature_names,
                                        class_names=class_names,
                                        filled=True,
                                        rounded=True)
graph = graphviz.Source(dot_data_minimal)
graph.render("images/fish_blurred_max_depth_{}.pdf".format(max_depth))
