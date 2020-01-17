# build a tree for fish
import numpy as np
import ipdb
from sklearn import tree
import graphviz
from sklearn.tree import DecisionTreeClassifier

fish_features = np.load("fish_features.npy")
fish_class = np.load("fish_class.npy")

feature_names = ["length", "weight"]
class_names = ["tuna", "salmon"]

max_depth = 2
classifier = tree.DecisionTreeClassifier(max_depth=max_depth, criterion="entropy")
classifier = classifier.fit(fish_features, fish_class)

# convert the graph to graphviz in order to visualize it
dot_data_minimal = tree.export_graphviz(classifier,
                                        out_file=None,
                                        feature_names=feature_names,
                                        class_names=class_names,
                                        filled=True,
                                        rounded=True)
graph = graphviz.Source(dot_data_minimal)
graph.render(f"images/fish_max_depth_{max_depth}.pdf"))

# predicion

# new fishes we want to classify with its features
# new_fish_1_length = 35
# new_fish_1_weight = 4
# new_fish_1 = np.array([[new_fish_1_length, new_fish_1_weight]])
# prediction = classifier.predict(new_fish_1)
# if prediction == 1:
#     predicted_class = "salmon"
# elif prediction == 0:
#     predicted_class = "tuna"
# else:
#     raise ValueError("wrong prediction")
# print("\nnew fish: {} centimeters, {} kilos".format(new_fish_1_length, new_fish_1_weight))
# print("the class predicted for the new fish is "+predicted_class)

# new_fish_2_length = 60
# new_fish_2_weight = 7
# new_fish_2 = np.array([[new_fish_2_length, new_fish_2_weight]])
# prediction = classifier.predict(new_fish_2)
# if prediction == 1:
#     predicted_class = "salmon"
# elif prediction == 0:
#     predicted_class = "tuna"
# else:
#     raise ValueError("wrong prediction")
# print("\nnew fish: {} centimeters, {} kilos".format(new_fish_2_length, new_fish_2_weight))
# print("the class predicted for the new fish is "+predicted_class)
