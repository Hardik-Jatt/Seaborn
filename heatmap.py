import seaborn as sns
import matplotlib.pyplot as plt

# Load the example dataset for flights
flights = sns.load_dataset('flights')

# Pivot the dataset
flights_pivot = flights.pivot('month', 'year', 'passengers')

# Create a heatmap
sns.heatmap(flights_pivot, cmap='coolwarm', annot=True, fmt='d')
plt.title('Heatmap')
plt.show()
