#bernoilli
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from sklearn.datasets import load_breast_cancer

# Load the breast cancer dataset
data = load_breast_cancer()

# Extract the target variable (0: benign, 1: malignant)
target = data.target

# Calculate the probability of having cancer
p = np.mean(target)

# Define the possible outcomes (0: no cancer, 1: cancer)
outcomes = [0, 1]

# Calculate the probability mass function (PMF) of the Bernoulli distribution
pmf = bernoulli.pmf(outcomes, p)

# Visualize the Bernoulli distribution
plt.bar(outcomes, pmf)
plt.xlabel("Outcome")
plt.ylabel("Probability")
plt.xticks(outcomes)
plt.title("Bernoulli Distribution: Breast Cancer")
plt.show()
