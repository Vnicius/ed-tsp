# -*- coding: utf-8 -*-


def calculate_cost(solution):
    cost = 0
    size_points = len(solution)

    for index in range(size_points):
        next_index = index + 1 if (index + 1) < size_points else 0

        next_neighbor = next((neighbor for neighbor in solution[index].neighborhood
                              if neighbor.node.key == solution[next_index].key))

        cost += next_neighbor.cost

    return cost


def swap_neighborhood(solution, i, j):
    solution[i], solution[j] = solution[j], solution[i]
    cost = calculate_cost(solution)

    return solution, cost


def solution_to_string(solution):
    return str([node.key for node in solution])
