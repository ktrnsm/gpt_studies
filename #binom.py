import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
target = data.target
num_cancer_patients = np.sum(target)
p = num_cancer_patients / len(target)
n = len(target)
k_values = np.arange(0, n+1)
pmf = binom.pmf(k_values, n, p)
plt.bar(k_values, pmf)
plt.xlabel("Number of Cancer Patients")
plt.ylabel("Probability")
plt.title("Binomial Distribution: Breast Cancer Patients")
plt.show()
