#possion
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
target = data.target
avg_cancer_patients = np.mean(target)
n = len(target)
k_values = np.arange(0, n+1)
pmf = poisson.pmf(k_values, avg_cancer_patients)
plt.bar(k_values, pmf)
plt.xlabel("Number of Cancer Patients")
plt.ylabel("Probability")
plt.title("Poisson Distribution: Breast Cancer Patients")
plt.show()
