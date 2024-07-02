import seaborn as sns
import matplotlib.pyplot as plt

# Load the example dataset for the tips
tips = sns.load_dataset('tips')

# Create a strip plot
sns.stripplot(x='day', y='total_bill', data=tips, jitter=True)
plt.title('Strip Plot')
plt.show()
