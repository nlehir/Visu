from sklearn.datasets import load_digits
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
redudant_data = np.load("redundant_data.npy")

pca = PCA().fit(redudant_data)

variance_ratio = pca.explained_variance_ratio_

nb_components = 6
plt.plot(range(1, nb_components+1),
         np.cumsum(variance_ratio[:nb_components]), "o")
plt.xticks(range(1, nb_components+1))
plt.title("variance in the projected data")
plt.xlabel('number of components')
plt.ylabel('cumulative explained variance')
plt.savefig("explained_variance_redundancy.pdf")
