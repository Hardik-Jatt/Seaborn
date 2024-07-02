import seaborn as sns
import matplotlib.pyplot as plt

# Load the example dataset for the tips
tips = sns.load_dataset('tips')

# Create a histogram
sns.histplot(tips['total_bill'], bins=30)
plt.title('Histogram')
plt.show()
