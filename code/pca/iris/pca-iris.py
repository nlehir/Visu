import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA

iris = datasets.load_iris()

X, Y = iris.data, iris.target
# used to differentiate the classes
colMap = {0: "red", 1: "green", 2: "black"}
colors = list(map(lambda x: colMap.get(x), Y))

# used to see if we can interpret the principal components
pca = PCA(n_components=2)
pca.fit(X)

# fit again PCA and project the data on
# the principal components
X_projected = PCA(n_components=2).fit_transform(X)

plt.scatter(X_projected[:, 0], X_projected[:, 1], alpha=0.7, c=colors)

plt.title("pcs iris")
plt.savefig("pca_iris.pdf")
