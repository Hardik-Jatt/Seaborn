import seaborn as sns
import matplotlib.pyplot as plt

# Load the example dataset for flights
flights = sns.load_dataset('flights')

# Create a line plot
sns.lineplot(x='year', y='passengers', data=flights)
plt.title('Line Plot')
plt.show()
