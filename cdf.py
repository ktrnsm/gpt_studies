import random
import matplotlib.pyplot as plt
def roll_dice():
    first_die = random.randint(1, 6)
    second_die = random.randint(1, 6)
    return first_die + second_die
def main():
    results = []
    for _ in range(100):
        result = roll_dice()
        results.append(result)
    cdf = {}
    for x in range(2, 13):
        cdf[x] = sum(results.count(y) for y in range(x)) / len(results)
    plt.plot(list(cdf.keys()), list(cdf.values()))
    plt.xlabel("Sum of two dice")
    plt.ylabel("Probability")
    plt.show()
if __name__ == "__main__":
    main()
