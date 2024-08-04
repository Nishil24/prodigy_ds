
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Example data
ages = np.random.randint(18, 80, size=100)  # Random ages between 18 and 80
# Plot the histogram
plt.hist(ages, bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution Histogram')
plt.show()

# Bar chart
data = {'Gender': ['Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Male']}
df = pd.DataFrame(data)
# Count the occurrences of each category
gender_counts = df['Gender'].value_counts()

# Plot the bar chart
gender_counts.plot(kind='bar', color=['blue', 'pink'])
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Gender Distribution Bar graph')
plt.show()