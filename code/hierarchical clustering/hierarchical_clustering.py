"""
    File illustrating hierarchical clustering.
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial
import seaborn as sns
import csv

# open file
file_name = 'addresses.csv'

x_coordinates = list()
y_coordinates = list()

# load the data
with open(file_name, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        x_coordinates.append(float(row[0]))
        y_coordinates.append(float(row[1]))

x_coordinates = np.asarray(x_coordinates)
y_coordinates = np.asarray(y_coordinates)
data = np.column_stack((x_coordinates, y_coordinates))

"""
    Part A : show a scatter plot of the data
"""
# # first method manual plot

"""
    Part B : hierarchical clustering.
    We will use agglomerative clustering.
"""
# choose metric
metric = "euclidean"

# build distance matrix between points
condensed_distance = scipy.spatial.distance.pdist(data, metric=metric)
distance_matrix = scipy.spatial.distance.squareform(condensed_distance)

# initializes classes
# each data point is its own class.
classes = list()
for class_index in range(nb_datapoints):
    classes.append([class_index])


def find_closest_classes(classes):
    min_dist = np.max(distance_matrix)
    returned_classes = (0, 1)
    """
        Add lines here
    """
    return returned_classes


def distance_between_classes_single_linkage(class_1, class_2):
    """
        single linkage clustering.
        The distance is the minimum distance between
        any point in class_1 and any point in class_2
    """
    min_dist = np.max(distance_matrix)
    """
        Add lines here
    """
    return min_dist


def distance_between_classes_average_linkage(class_1, class_2):
    """
        average linkage clustering
        The distance is the average of distances between
        apoint in class_1 a point in class_2
    """
    min_dist = np.max(distance_matrix)
    distances = list()
    distances.append(1)
    """
        Add lines here
    """
    average_distances = sum(distances)/len(distances)
    return average_distances


def define_color(index):
    int_1 = (3*index) % 9+1
    int_2 = (3*index) % 5+1
    int_3 = (3*index) % 2+1


def plot_clustering(step, classes):
    plt.plot(x_coordinates, y_coordinates, "o")
    for index in range(len(classes)):
        class_to_plot = classes[index]
        x_coord = x_coordinates[class_to_plot]
        y_coord = y_coordinates[class_to_plot]
        color = define_color(index)
        plt.plot(x_coord, y_coord, "o", color=color)
    plt.title(f"hierarchical clustering\nstep {step}"\
              f"\n{len(classes)} clusters\n"\
             f"{metric} metric")
    plt.tight_layout()
    plt.savefig(f"clustering/clustering_step_{step}.pdf")
    plt.close()


step = 0
while len(classes) > 1:
    step += 1
    index_1, index_2 = find_closest_classes(classes)
    classes[index_1] = classes[index_1]+classes[index_2]
    classes.remove(classes[index_2])
    plot_clustering(step, classes)
