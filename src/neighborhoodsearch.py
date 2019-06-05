# -*- coding: utf-8 -*-

from copy import copy
from src.utils.utils import calculate_cost, swap_neighborhood
import random


def best_improvement_method(initial_solution, distance_table):
    """Try to search the best solution in the neighborhood

    Arguments:
        initial_solution {list} -- list with initial solution
        distance_table {list} -- matrix with the distances values

    Returns:
        list -- solution founded
    """

    current_solution = copy(
        initial_solution)       # Copy initial solution as current solution
    # Caculate the cost of the solution
    min_cost = calculate_cost(initial_solution, distance_table)
    size_points = len(initial_solution)     # Get the number of points
    has_new_search = True      # Check if has to make a new search

    while has_new_search:
        has_new_search = False

        for i in range(size_points - 1):
            for j in range(i+1, size_points - 1):

                # Search a candidate in the neighborhood
                candidate_solution, candidate_cost = swap_neighborhood(
                    copy(current_solution), distance_table, i, j)

                # Check if the candidate's cost is the lowest
                if candidate_cost < min_cost:
                    has_new_search = True
                    min_cost = candidate_cost       # Change the lowest cost
                    current_solution = candidate_solution     # Change the best solution

    return current_solution


def first_improvement_method(initial_solution, distance_table):
    """Try to search the first best solution in the neighborhood

    Arguments:
        initial_solution {list} -- list with initial solution
        distance_table {list} -- matrix with the distances values

    Returns:
        list -- solution founded
    """

    current_solution = copy(
        initial_solution)       # Copy initial solution as current solution
    # Caculate the cost of the solution
    min_cost = calculate_cost(initial_solution, distance_table)
    size_points = len(initial_solution)     # Get the number of points
    has_new_search = True      # Check if has to make a new search

    while has_new_search:
        has_new_search = False
        # Select a random index to start
        start_index = random.randint(0, size_points)
        index_sequence = list(range(start_index, size_points)
                              ) + list(range(0, start_index))       # Make a new list of indexes
        random.shuffle(index_sequence)

        for i in index_sequence:
            for j in range(i+1, size_points - 1):

                # Search a candidate in the neighborhood
                candidate_solution, candidate_cost = swap_neighborhood(
                    copy(current_solution), distance_table, i, j)

                #print(candidate_cost, min_cost)
                # Check if the candidate's cost is the lowest
                if candidate_cost < min_cost:
                    has_new_search = True
                    min_cost = candidate_cost       # Change the lowest cost
                    current_solution = candidate_solution     # Change the best solution
                    break       # Break in the first improvement

            if has_new_search:
                break       # Break in the first improvement

    return current_solution


def random_method(initial_solution, distance_table, limit=5):
    """Search the best solution in random neighbours

    Arguments:
        initial_solution {list} -- list with initial solution
        distance_table {list} -- matrix with the distances values

    Keyword Arguments:
        limit {int} -- limit of not improvements (default: {5})

    Returns:
        list -- solution founded
    """
    current_solution = copy(
        initial_solution)       # Copy initial solution as current solution
    # Caculate the cost of the solution
    min_cost = calculate_cost(initial_solution, distance_table)
    count = 0

    while count < limit:
        candidate_solution = copy(current_solution)
        random.shuffle(candidate_solution)      # Generate a radom candidate
        # Calculate the candidate's cost
        candidate_cost = calculate_cost(candidate_solution, distance_table)

        # Check if the candidate's cost is the lowest
        if candidate_cost <= min_cost:
            min_cost = candidate_cost       # Change the lowest cost
            current_solution = candidate_solution     # Change the best solution
            count = 0       # Reboot the count
        else:
            count += 1      # Add 1 if not improve

    return current_solution


def vnd_method(initial_solution, distance_table, samples=5):
    """Search the best solution in random neighbours

    Arguments:
        initial_solution {list} -- list with initial solution
        distance_table {list} -- matrix with the distances values

    Keyword Arguments:
        samples {int} -- number of set of neighborhoods to search (default: {5})

    Returns:
        list -- solution founded
    """
    current_solution = copy(
        initial_solution)       # Copy initial solution as current solution
    # Caculate the cost of the solution
    min_cost = calculate_cost(initial_solution, distance_table)
    k = 0

    while k < samples:
        # Search the best solution in the neighborhood
        best_candidate = random_method(
            current_solution, distance_table, limit=k)
        # Calculate the candidate's cost
        candidate_cost = calculate_cost(best_candidate, distance_table)

        # Check if the candidate's cost is the lowest
        if candidate_cost < min_cost:
            # Define the candidate solution as the current solution
            current_solution = best_candidate
            min_cost = candidate_cost       # Define the candidate's cost as the lowest
            k = 0       # Reboot the count
        else:
            k += 1      # Add 1 if not improve

    return current_solution
