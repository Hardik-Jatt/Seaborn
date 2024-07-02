import seaborn as sns
import matplotlib.pyplot as plt

# Load the example dataset for the tips
tips = sns.load_dataset('tips')

# Create a swarm plot
sns.swarmplot(x='day', y='total_bill', data=tips)
plt.title('Swarm Plot')
plt.show()
