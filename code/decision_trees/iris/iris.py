# import ipdb
from sklearn import tree
from sklearn.datasets import load_iris
import graphviz
from sklearn.tree import DecisionTreeClassifier
# import sklearn.tree.export
# from sklearn.tree.export import export_text

iris = load_iris()
our_tree = tree.DecisionTreeClassifier()
our_tree = our_tree.fit(iris.data, iris.target)

# plot the graph
dot_data = tree.export_graphviz(our_tree,
                                out_file=None,
                                feature_names=iris.feature_names,
                                class_names=iris.target_names,
                                filled=True,
                                rounded=True,
                                special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("iris")
