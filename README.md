# Project Title: Knapsack Optimization Using Dynamic Programming and Ant Colony Optimization (ACO)

---

## Overview

This project solves the Knapsack Problem using two algorithms:

1. **Dynamic Programming (DP)**: A classic approach to maximize the value of selected items without exceeding the weight capacity.
2. **Ant Colony Optimization (ACO)**: A metaheuristic algorithm inspired by the behavior of ants in finding optimal paths, applied here to select the best combination of items.

Both approaches are implemented to solve the same problem, allowing comparison of results and insights into their respective performance.

---

## Problem Description

The Knapsack Problem involves:

- **Input**: 
  - A fixed **capacity** of the knapsack (295 units in this case).
  - A list of **items** (bags), each with a specific weight and value.
- **Output**: 
  - The **maximum total value** that can be achieved without exceeding the knapsack's capacity.
  - The **list of selected items** contributing to this maximum value.

---

## Implementation Details

### 1. **Dynamic Programming**

- **Objective**: Systematically evaluate all possible combinations to maximize the total value.
- **Approach**:
  - A 2D table `dp[i][w]` stores the maximum value achievable with the first `i` items and a knapsack capacity of `w`.
  - Iterative updates ensure that for each item, either it is included (if capacity allows) or excluded to maximize the value.
  - Convergence behavior is plotted to observe how quickly the algorithm stabilizes.

### 2. **Ant Colony Optimization (ACO)**

- **Objective**: Use probabilistic decision-making to simulate the behavior of ants searching for the best paths.
- **Approach**:
  - Each "ant" selects items based on a combination of pheromone levels and heuristic information (item values).
  - Pheromones are updated iteratively based on the quality of solutions discovered.
  - Parameters include:
    - `alpha`: Importance of pheromone influence.
    - `beta`: Importance of heuristic value.
    - `rho`: Evaporation rate of pheromones.
  - The best solution across iterations is tracked and returned.

---

## Project Files

- **Source Code**: Python implementation of both algorithms.
- **Requirements**:
  - `matplotlib`: For visualization of convergence.
  - `numpy`: For efficient numerical computations.
  - `seaborn`: For additional visualization styling.
- **Output**:
  - Maximum value achievable.
  - List of selected items for the maximum value.
  - Convergence plot for the DP algorithm.

---

## Results
![download](https://github.com/user-attachments/assets/0315a7cc-3f30-4061-a27c-42b916be16f5)
![Screenshot 2024-12-01 234523](https://github.com/user-attachments/assets/d2def01a-1b60-497b-bce8-d80b17f30b26)

# Results Summary

## Dynamic Programming

- **Maximum Value Achieved**: 4333
- **Selected Bags**:  
  The following bag indices (representing the optimal set of items) were chosen to maximize the value without exceeding the knapsack's capacity:  
  `[100, 99, 96, 95, 91, 90, 89, 87, 84, 83, 80, 78, 77, 76, 74, 73, 69, 67, 66, 65, 63, 62, 61, 60, 59, 58, 57, 56, 54, 53, 51, 50, 48, 47, 46, 45, 44, 42, 40, 38, 37, 36, 34, 33, 32, 31, 29, 28, 27, 25, 24, 21, 20, 19, 16, 15, 11, 9, 8, 6, 5, 4, 3, 2, 1]`

### Key Observations:
- Dynamic Programming explores all possible combinations to find the optimal solution.
- The algorithm achieved a significantly higher total value compared to ACO by exhaustively searching the solution space.

---

## Ant Colony Optimization (ACO)

- **Maximum Value Achieved**: 430
- **Selected Bags**:  
  The following bag indices were chosen by the ant colony optimization algorithm:  
  `[10, 19, 47, 61, 65]`

### Key Observations:
- ACO uses probabilistic decision-making and heuristic search rather than exhaustive exploration.
- The solution is suboptimal compared to Dynamic Programming but showcases the strengths of ACO in handling large-scale problems quickly and efficiently when exhaustive search is impractical.

---

## Comparison of Approaches

| Feature                     | Dynamic Programming        | Ant Colony Optimization |
|-----------------------------|----------------------------|--------------------------|
| **Maximum Value**           | 4333                       | 430                      |
| **Execution Time**          | Longer due to exhaustive search | Faster due to heuristic-based search |
| **Scalability**             | Poor for large datasets    | Good for large datasets  |
| **Deterministic Solution**  | Yes                        | No (probabilistic results) |

Dynamic Programming excels in accuracy, while Ant Colony Optimization demonstrates efficiency in scenarios with larger datasets or more complex constraints.



