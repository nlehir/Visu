import ipdb
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="ticks")

# load the dataset
df = sns.load_dataset("iris")

# pairplot is the name of the seaborn function
# to plot the scatter matrix
sns.pairplot(df, hue="species")

title = 'Scatter matrix of the iris dataset'
file = 'iris_scatter_matrix.pdf'
plt.title(title)
plt.savefig(file)
