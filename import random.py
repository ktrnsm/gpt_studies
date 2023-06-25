import random
from collections import Counter
import matplotlib.pyplot as plt

# Number of coin flips
num_flips = 10

# Simulate flipping a coin num_flips times
flips = [random.choice(["Heads", "Tails"]) for _ in range(num_flips)]

# Count the occurrences of each outcome
outcome_counts = Counter(flips)

# Display the table content
print("Table Content (Discrete Random Variable):")
print("{:<10s} {:<10s}".format("Outcome", "Count"))
for outcome, count in outcome_counts.items():
    print("{:<10s} {:<10d}".format(outcome, count))

# Visualize the results
outcomes = outcome_counts.keys()
counts = outcome_counts.values()

plt.bar(outcomes, counts)
plt.xlabel('Outcome')
plt.ylabel('Count')
plt.title('Discrete Random Variable')
plt.show()
