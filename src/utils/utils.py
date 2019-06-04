# -*- coding: utf-8 -*-

def calculate_cost(solution, distance_matrix):
    cost = 0
    size_points = len(solution)

    for index in range(size_points):
        next_index = index if (index + 1) < size_points else 0

        cost += distance_matrix[solution[index]][solution[next_index]]

    return cost 

def swap_neighborhood(solution, distance_matrix, i, j):
    solution[i], solution[j] = solution[j], solution[i]
    cost = calculate_cost(solution, distance_matrix)

    return solution, cost
