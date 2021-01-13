import numpy as np
import matplotlib.pyplot as plt

data = np.load("data.npy")

fig = plt.figure()


def plot_data_point(datapoint, fig):
    """
        Add lines here
    """
    pass


for point_index in range(data.shape[0]):
    """
        Edit function
    """
    plot_data_point(1, fig)


labels = ["Var 1", "Var 2", "Var 3", "Var 4"]
plt.title("parallel coordinate plot")
plt.xticks([0, 1, 2, 3], labels=labels)
plt.savefig("parallel_coordinates.pdf")
plt.close()
