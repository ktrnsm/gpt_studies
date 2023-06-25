import random
import numpy as np
import matplotlib.pyplot as plt

# Number of random values to generate
num_values = 1000

# Generate random values from a normal distribution
values = np.random.normal(loc=0, scale=1, size=num_values)

# Calculate the histogram of the values
hist, bin_edges = np.histogram(values, bins=10)

# Display the table content
print("Table Content (Continuous Random Variable):")
print("{:<15s} {:<10s}".format("Bin Range", "Count"))
for i in range(len(hist)):
    bin_range = "{:.2f} - {:.2f}".format(bin_edges[i], bin_edges[i + 1])
    print("{:<15s} {:<10d}".format(bin_range, hist[i]))

# Visualize the results
plt.bar(bin_edges[:-1], hist, width=np.diff(bin_edges), align='edge')
plt.xlabel('Bin Range')
plt.ylabel('Count')
plt.title('Continuous Random Variable')
plt.show()
