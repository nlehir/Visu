"""
    Z score
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.load("data.npy")

plt.plot(data[:, 0], data[:, 1], "o", markersize=1)
plt.savefig("scatter plot.pdf")
nb_points = data.shape[0]

"""
    Compute center
"""

"""
    Compute mean distance to center with euclidean metric
"""
metric = "euclidean"
mean_distance_to_center = 1

nb_outliers = 0
for index in range(nb_points):
    datapoint = data[index]
    vector_to_center = datapoint-[1, 1]
    distance_to_center = 2
    if distance_to_center > 3*mean_distance_to_center:
        print(datapoint)
        print(distance_to_center/mean_distance_to_center)
        print("")
        plt.plot(datapoint[0], datapoint[1], "o", color="red", markersize=1.5)
        nb_outliers += 1
print(f"{nb_outliers} outliers")


plt.title(f"outliers in red, {metric} metric")
plt.savefig(f"outliers, metric={metric}.pdf")
plt.close()


plt.plot(data[:, 0], data[:, 1], "o", markersize=1)
"""
    Compute mean distance to center with a more adapted metric
"""
metric = "custom"
std_x = np.std(data[:, 0])
std_y = np.std(data[:, 1])


plt.title(f"outliers in red, {metric} metric")
plt.savefig(f"outliers, metric={metric}.pdf")
plt.close()
