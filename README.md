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
