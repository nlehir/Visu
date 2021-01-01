from sklearn.datasets import load_digits
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
digits = load_digits()

# the data consists in 1797 samples
# of 8*8 pixels images

pca = PCA().fit(digits.data)

variance_ratio = pca.explained_variance_ratio_

nb_components = 20
plt.plot(range(1, nb_components+1),
         np.cumsum(variance_ratio[:nb_components]), "o")
plt.xticks(range(1, nb_components+1))
plt.title("variance in the projected data")
plt.xlabel('number of components')
plt.ylabel('cumulative explained variance')
plt.savefig("explained_variance.pdf")
