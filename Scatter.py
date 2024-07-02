import seaborn as sns
import matplotlib.pyplot as plt

# Load the example dataset for the tips
tips = sns.load_dataset('tips')

# Create a scatter plot
sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.title('Scatter Plot')
plt.show()
