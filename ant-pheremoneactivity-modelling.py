import matplotlib.pyplot as plt
import numpy as np

# Define van capacity and bags
capacity = 295
bags = [
    (9.4, 57), (7.4, 94), (7.7, 59), (7.4, 83), (2.9, 82), (1.1, 91), (7.3, 42), (9.0, 84),
    (8.1, 85), (7.2, 18), (7.5, 94), (4.2, 18), (4.4, 31), (5.7, 27), (2.0, 31), (2.0, 42),
    (9.9, 58), (9.5, 57), (5.2, 55), (7.1, 97), (6.8, 79), (1.6, 10), (7.9, 34), (3.0, 100),
    (1.6, 98), (9.0, 45), (2.1, 19), (4.9, 77), (7.0, 56), (6.8, 25), (7.7, 60), (2.1, 22),
    (8.4, 84), (1.9, 89), (6.5, 12), (3.8, 46), (2.5, 20), (4.3, 85), (9.9, 42), (8.5, 94),
    (8.0, 20), (1.0, 65), (4.4, 27), (2.6, 34), (2.1, 27), (7.4, 91), (1.5, 17), (2.2, 56),
    (8.1, 23), (7.9, 89), (1.5, 18), (3.5, 11), (2.4, 91), (1.6, 79), (4.3, 14), (7.5, 99),
    (2.5, 45), (7.6, 73), (4.8, 81), (6.5, 96), (1.5, 51), (2.3, 96), (1.0, 63), (8.1, 40),
    (8.1, 93), (6.7, 87), (5.8, 71), (7.7, 54), (4.9, 74), (1.6, 15), (6.5, 32), (7.4, 57),
    (1.4, 70), (4.1, 62), (7.4, 12), (7.4, 71), (1.7, 57), (1.2, 97), (9.5, 48), (1.9, 33),
    (7.5, 42), (6.1, 25), (5.9, 59), (3.7, 91), (7.5, 17), (9.0, 63), (1.7, 81), (7.9, 49),
    (1.5, 60), (7.8, 90), (7.6, 87), (9.3, 25), (9.8, 15), (8.0, 20), (3.3, 76), (3.9, 76),
    (9.6, 53), (7.1, 59), (3.9, 40), (3.9, 59)
]

# Number of bags
num_bags = len(bags)

# ============================= Dynamic Programming =============================
dp = [[0 for _ in range(int(capacity) + 1)] for _ in range(num_bags + 1)]
dp_convergence = []

for i in range(1, num_bags + 1):
    weight, value = bags[i-1]
    for w in range(int(capacity) + 1):
        if weight <= w:
            dp[i][w] = max(dp[i-1][w], dp[i-1][int(w-weight)] + value)
        else:
            dp[i][w] = dp[i-1][w]
    dp_convergence.append(max(dp[i]))

max_value_dp = dp[num_bags][int(capacity)]

# Find selected bags for DP
selected_bags_dp = []
w = capacity
for i in range(num_bags, 0, -1):
    if dp[i][int(w)] != dp[i-1][int(w)]:
        selected_bags_dp.append(i)
        w -= bags[i-1][0]

# ======================== Ant Colony Optimization (ACO) ========================
def aco_algorithm(num_ants, num_iterations, alpha=1.0, beta=2.0, rho=0.5):
    pheromone = np.ones(num_bags)
    heuristic = np.array([bag[1] for bag in bags])
    best_value = 0
    best_selection = []

    for _ in range(num_iterations):
        for _ in range(num_ants):
            probabilities = (pheromone**alpha) * (heuristic**beta)
            probabilities /= probabilities.sum()

            selection = []
            remaining_capacity = capacity
            for i in range(num_bags):
                if remaining_capacity >= bags[i][0]:
                    if np.random.rand() < probabilities[i]:
                        selection.append(i)
                        remaining_capacity -= bags[i][0]

            selection_value = sum([bags[i][1] for i in selection])
            if selection_value > best_value:
                best_value = selection_value
                best_selection = selection

        pheromone = (1 - rho) * pheromone
        for i in best_selection:
            pheromone[i] += 1

    return best_value, best_selection

num_ants = 50
num_iterations = 100
max_value_aco, selected_bags_aco = aco_algorithm(num_ants, num_iterations)

# ============================ Plot and Compare ================================
plt.figure(figsize=(12, 6))
plt.plot(dp_convergence, label="Dynamic Programming", color='green', linewidth=2)
plt.axhline(y=max_value_aco, color='blue', linestyle='--', label="ACO Maximum Value")
plt.title("Convergence of DP and ACO for the Knapsack Problem")
plt.xlabel("Iterations")
plt.ylabel("Maximum Value")
plt.legend()
plt.grid(True)
plt.show()

# ============================= Output Results ================================
print("Dynamic Programming:")
print("Maximum value:", max_value_dp)
print("Selected bags:", selected_bags_dp)

print("\nAnt Colony Optimization:")
print("Maximum value:", max_value_aco)
print("Selected bags:", selected_bags_aco)
