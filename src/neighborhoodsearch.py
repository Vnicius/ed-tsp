# -*- coding: utf-8 -*-

from copy import copy
from src.utils.utils import calculate_cost, swap_neighborhood
import random

def best_improvement_method(initial_solution, distance_table):
    current_solution = copy(initial_solution)
    min_cost = calculate_cost(initial_solution, distance_table)
    size_points = len(initial_solution)
    is_best = True

    while is_best:
        is_best = False
        best_candidate = current_solution

        for i in range(size_points - 1):
            for j in range(i+1, size_points - 1):
                candidate_solution, candidate_cost = swap_neighborhood(copy(current_solution), distance_table, i, j)

                if candidate_cost < min_cost:
                    is_best = True
                    min_cost = candidate_cost
                    best_candidate = candidate_solution
        
        current_solution = best_candidate
    
    return current_solution


def first_improvement_method(initial_solution, distance_table):
    current_solution = copy(initial_solution)
    min_cost = calculate_cost(initial_solution, distance_table)
    size_points = len(initial_solution)
    is_best = True

    while is_best:
        is_best = False
        best_candidate = current_solution
        start_index = random.randint(0, size_points)
        index_sequence = list(range(start_index, size_points)) + list(range(0, start_index))

        for i in index_sequence:
            for j in range(i+1, size_points - 1):
                candidate_solution, candidate_cost = swap_neighborhood(copy(current_solution), distance_table, i, j)

                if candidate_cost < min_cost:
                    is_best = True
                    min_cost = candidate_cost
                    best_candidate = candidate_solution
                    break
            
            if is_best:
                break
        
        current_solution = best_candidate
    
    return current_solution



