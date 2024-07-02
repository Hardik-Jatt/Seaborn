import seaborn as sns
import matplotlib.pyplot as plt

# Load the example dataset for the iris
iris = sns.load_dataset('iris')

# Create a pair plot
sns.pairplot(iris)
plt.title('Pair Plot')
plt.show()
