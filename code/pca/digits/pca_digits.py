from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
digits = load_digits()

# the data consists in 1797 samples
# of 8*8 pixels images
print(digits.data.shape)

# we use PCA in order to project them
# on principal components
pca = PCA(n_components=2)
projected_data = pca.fit_transform(digits.data)

print(projected_data.shape)


plt.scatter(projected_data[:, 0], projected_data[:, 1],
            c=digits.target, edgecolor='none', alpha=0.5,
            cmap=plt.cm.get_cmap('jet', 10))
plt.xlabel('component 1')
plt.ylabel('component 2')
plt.colorbar()

plt.savefig("projected_digits.pdf")
