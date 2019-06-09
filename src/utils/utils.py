# -*- coding: utf-8 -*-
import numpy as np


def calculate_cost(solution):
    cost = 0
    size_points = len(solution)

    for index in range(size_points):
        next_index = index + 1 if (index + 1) < size_points else 0
        next_node = solution[next_index].key

        next_neighbor = solution[index].neighborhood[next_node]

        cost += next_neighbor.cost

    return cost


def __get_index_neighborhood(solution, index):
    prev_node = solution[index - 1].key if index > 0 else -1
    node = solution[index].key
    next_node = solution[index + 1 if index + 1 < len(solution) else 0].key

    return prev_node, node, next_node


def __get_cost(node, prev_key, next_key):
    cost = 0

    if prev_key != -1:
        cost += node.neighborhood[prev_key].cost
    cost += node.neighborhood[next_key].cost

    return cost


# def calculate_swap_cost(solution, i, j):

#     prev_i, i_key, next_i = __get_index_neighborhood(solution, i)
#     prev_j, j_key, next_j = __get_index_neighborhood(solution, j)
#     i_node = solution[i]
#     j_node = solution[j]

#     old_i_cost = __get_cost(i_node, prev_i, next_i)
#     old_j_cost = __get_cost(j_node, prev_j, next_j)
#     new_i_cost = 0
#     new_j_cost = 0
#     diff_return_cost = 0

#     if j - i == 1:
#         prev_j = j_key
#         next_i = i_key
#     elif j == len(solution) - 1 and i == 0:
#         next_j = j_key

#     new_i_cost = __get_cost(j_node, prev_i, next_i)
#     new_j_cost = __get_cost(i_node, prev_j, next_j)

#     if i == 0 and j != len(solution) - 1:
#         old_return_cost = solution[-1].neighborhood[i_key].cost
#         new_return_cost = solution[-1].neighborhood[j_key].cost
#         diff_return_cost = new_return_cost - old_return_cost

#     return (new_i_cost - old_i_cost) + (new_j_cost - old_j_cost) + diff_return_cost


def calculate_swap_cost(solution, i, j, is_2opt=False):

    prev_i, i_key, next_i = __get_index_neighborhood(solution, i)
    prev_j, j_key, next_j = __get_index_neighborhood(solution, j)
    i_node = solution[i]
    j_node = solution[j]

    old_i_cost = __get_cost(i_node, prev_i, next_i)
    old_j_cost = __get_cost(j_node, prev_j, next_j)
    new_i_cost = 0
    new_j_cost = 0
    diff_return_cost = 0

    if is_2opt:
        next_i, prev_j = prev_j, next_i

    if j - i == 1:
        prev_j = j_node.key
        next_i = i_node.key
    elif j == len(solution) - 1 and i == 0:
        next_j = j_node.key

    new_i_cost = __get_cost(j_node, prev_i, next_i)
    new_j_cost = __get_cost(i_node, prev_j, next_j)

    if i == 0 and j != len(solution) - 1:
        old_return_cost = solution[-1].neighborhood[i_key].cost
        new_return_cost = solution[-1].neighborhood[j_key].cost
        diff_return_cost = new_return_cost - old_return_cost

    return (new_i_cost - old_i_cost) + (new_j_cost - old_j_cost) + diff_return_cost


def get_neighbor(node, key):
    return next((neighbor for neighbor in node.neighborhood
                 if neighbor.node.key == key))


def swap_neighborhood(solution, i, j):
    solution[i], solution[j] = solution[j], solution[i]

    return solution


def swap_2opt(solution, i, j):
    if i == 0:
        solution[i:j+1] = solution[j::-1]
    else:
        solution[i:j+1] = solution[j:i-1:-1]

    return solution


def solution_to_string(solution):
    return str([node.key for node in solution])
