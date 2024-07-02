import seaborn as sns
import matplotlib.pyplot as plt

# Load the example dataset for the tips
tips = sns.load_dataset('tips')

# Create a bar plot
sns.barplot(x='day', y='total_bill', data=tips)
plt.title('Bar Plot')
plt.show()
