import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA

iris = datasets.load_iris()

X, Y = iris.data, iris.target
colMap = {0: "red", 1: "green", 2: "black"}
colors = list(map(lambda x: colMap.get(x), Y))
X_2ev = PCA(n_components=2).fit_transform(X)

plt.scatter(X_2ev[:, 0], X_2ev[:, 1], alpha=0.7, c=colors)

plt.title("pcs iris")
plt.savefig("pca_iris.pdf")
