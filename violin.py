import seaborn as sns
import matplotlib.pyplot as plt

# Load the example dataset for the tips
tips = sns.load_dataset('tips')

# Create a violin plot
sns.violinplot(x='day', y='total_bill', data=tips)
plt.title('Violin Plot')
plt.show()
