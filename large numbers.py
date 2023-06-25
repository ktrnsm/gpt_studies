import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
num_rolls = 100000
rolls = []
averages = []
for i in range(1, num_rolls + 1):
    roll = random.randint(1, 6)
    rolls.append(roll)
    average = np.mean(rolls)
    averages.append(average)
    if i % 100000 == 0:
        plt.figure()
        sns.lineplot(x=range(i), y=rolls, color='blue', label='Roll')
        sns.lineplot(x=range(i), y=averages, color='red', label='Average')
        plt.xlabel('Number of Rolls')
        plt.ylabel('Value')
        plt.title('Roll Results and Average')
        plt.legend()
        plt.show()
