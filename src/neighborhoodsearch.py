# -*- coding: utf-8 -*-

from copy import copy
from src.utils.utils import calculate_cost, swap_neighborhood, solution_to_string, calculate_swap_cost, swap_2opt
from src.utils.plotsolution import plot_animated
from src.ConstructionHeuristic import ConstructionHeuristic
import random


def swap_method(initial_solution, is_first=False, has_animation=False, title="Swap Method"):
    """Search a new solution for TSP with swap method

    Arguments:
        initial_solution {list} -- initial solution

    Keyword Arguments:
        is_first {bool} -- if will use the First Improvement (default: {False})
        has_animation {bool} -- if will the animate the search (default: {False})
        title {str} -- title of the animation (default: {"Best Improvement Method"})

    Returns:
        list -- the founded solution
    """
    current_solution = copy(
        initial_solution)       # Copy initial solution as current solution
    # Caculate the cost of the solution
    min_cost = calculate_cost(initial_solution)
    size_points = len(initial_solution)     # Get the number of points
    has_improvement = True      # Check if has improvement

    while has_improvement:
        has_improvement = False

        for i in range(size_points - 1):
            for j in range(i+1, size_points):

                # Calculate swap cost
                candidate_cost = min_cost + calculate_swap_cost(
                    current_solution, i, j)

                # Check if the candidate's cost is the lowest
                if candidate_cost < min_cost:
                    has_improvement = True
                    min_cost = candidate_cost      # Change the lowest cost
                    current_solution = swap_neighborhood(
                        current_solution, i, j)     # Change the best solution
                    if is_first:
                        break

            if has_animation:
                plot_animated(current_solution, title=title,
                              has_points=False, show_key=True)

            if is_first and has_improvement:
                break

    return current_solution


# def random_method(initial_solution, limit=5, has_animation=False, title="Random Method"):
#     """Search the best solution in random neighbours

#     Arguments:
#         initial_solution {list} -- list with initial solution

#     Keyword Arguments:
#         limit {int} -- limit of not improvements (default: {5})

#     Returns:
#         list -- solution founded
#     """
#     current_solution = copy(
#         initial_solution)       # Copy initial solution as current solution
#     # Caculate the cost of the solution
#     min_cost = calculate_cost(initial_solution)
#     count = 0

#     while count < limit:
#         candidate_solution = copy(current_solution)
#         random.shuffle(candidate_solution)      # Generate a radom candidate
#         # Calculate the candidate's cost
#         candidate_cost = calculate_cost(candidate_solution)

#         # Check if the candidate's cost is the lowest
#         if candidate_cost <= min_cost:
#             min_cost = candidate_cost       # Change the lowest cost
#             current_solution = candidate_solution     # Change the best solution
#             count = 0       # Reboot the count
#         else:
#             count += 1      # Add 1 if not improve

#         if has_animation:
#             plot_animated(current_solution, title=title,
#                           has_points=False, show_key=True)

#     return current_solution


def two_opt_method(initial_solution, is_first=False, has_animation=False, title="2-OPT Method"):
    """Search a new solution for TSP with 2-OPT method

    Arguments:
        initial_solution {list} -- initial solution

    Keyword Arguments:
        is_first {bool} -- if will use the First Improvement (default: {False})
        has_animation {bool} -- if will the animate the search (default: {False})
        title {str} -- title of the animation (default: {"Best Improvement Method"})

    Returns:
        list -- the founded solution
    """
    current_solution = copy(
        initial_solution)       # Copy initial solution as current solution
    # Caculate the cost of the solution
    min_cost = calculate_cost(initial_solution)
    size_points = len(initial_solution)     # Get the number of points
    has_improvement = True      # Check if has improvement
    has_points = current_solution[0].point != None

    while has_improvement:
        has_improvement = False

        for i in range(size_points - 1):
            for j in range(i+1, size_points):

                # Swap
                candidate_cost = min_cost + \
                    calculate_swap_cost(current_solution, i, j, True)

                # Check if the candidate's cost is the lowest
                if candidate_cost < min_cost:
                    has_improvement = True
                    min_cost = candidate_cost       # Change the lowest cost
                    # Change the best solution
                    current_solution = swap_2opt(current_solution, i, j)

                    if is_first:
                        break

            if has_animation:
                plot_animated(current_solution, title=title,
                              has_points=has_points, show_key=(not has_points))

            if is_first and has_improvement:
                break

    return current_solution


def vnd_method(initial_solution, methods, has_animation=False, title="VND Method"):
    """Search a new solution for TSP with VND method

    Arguments:
        initial_solution {list} -- initial solution
        methods {list} -- list with the sequence of the methods to be used

    Keyword Arguments:
        has_animation {bool} -- if will the animate the search (default: {False})
        title {str} -- title of the animation (default: {"Best Improvement Method"})

    Returns:
        list -- the founded solution
    """
    current_solution = copy(
        initial_solution)       # Copy initial solution as current solution
    # Caculate the cost of the solution
    min_cost = calculate_cost(initial_solution)
    k = 0
    methods_dict = {'swap': swap_method, '2opt': two_opt_method}

    while k < len(methods):

        # Search the best solution in the neighborhood
        is_first = True if 'fi' in methods[k] else False
        selected_method = ""

        if 'swap' in methods[k]:
            selected_method = 'swap'
        elif '2opt' in methods[k]:
            selected_method = '2opt'

        best_candidate = methods_dict[selected_method](
            current_solution, is_first=is_first, has_animation=has_animation, title=title)
        # Calculate the candidate's cost
        candidate_cost = calculate_cost(best_candidate)

        # Check if the candidate's cost is the lowest
        if candidate_cost < min_cost:
            # Define the candidate solution as the current solution
            current_solution = best_candidate
            min_cost = candidate_cost       # Define the candidate's cost as the lowest
            k = 0       # Reboot the count
        else:
            k += 1      # Add 1 if not improve

    return current_solution


def vns_method(initial_solution, vnd_methods, interations=5, has_animation=False, title="VNS Method"):
    """Search a new solution for TSP with VND method

    Arguments:
        initial_solution {list} -- initial solution
        methods {list} -- list with the sequence of the methods to be used

    Keyword Arguments:
        has_animation {bool} -- if will the animate the search (default: {False})
        title {str} -- title of the animation (default: {"Best Improvement Method"})

    Returns:
        list -- the founded solution
    """
    current_solution = copy(
        initial_solution)       # Copy initial solution as current solution
    # Caculate the cost of the solution
    min_cost = calculate_cost(initial_solution)
    k = 0
    size = len(current_solution)

    while k < interations:
        i_index = random.randint(0, size - 2)
        j_index = random.randint(i_index, size - 1)

        initial_candidate = swap_2opt(
            current_solution[:], i_index, j_index)  # pertubation

        candidate_solution = vnd_method(
            initial_candidate, vnd_methods, has_animation, title)

        # Calculate the candidate's cost
        candidate_cost = calculate_cost(candidate_solution)

        # Check if the candidate's cost is the lowest
        if candidate_cost < min_cost:
            # Define the candidate solution as the current solution
            current_solution = candidate_solution
            min_cost = candidate_cost       # Define the candidate's cost as the lowest
            k = 0       # Reboot the count
        else:
            k += 1      # Add 1 if not improve

    return current_solution


def grasp_method(initial_solution, vnd_methods, instance, interations=5, has_animation=False, title="VNS Method"):
    """Search a new solution for TSP with VND method

    Arguments:
        initial_solution {list} -- initial solution
        methods {list} -- list with the sequence of the methods to be used

    Keyword Arguments:
        has_animation {bool} -- if will the animate the search (default: {False})
        title {str} -- title of the animation (default: {"Best Improvement Method"})

    Returns:
        list -- the founded solution
    """
    current_solution = copy(
        initial_solution)       # Copy initial solution as current solution
    # Caculate the cost of the solution
    min_cost = calculate_cost(initial_solution)
    k = 0
    size = len(current_solution)
    construction = ConstructionHeuristic()

    while k < interations:
        i = random.randint(0, size - 1)

        initial_candidate = construction.construct_nearest(instance, i)

        candidate_solution = vnd_method(
            initial_candidate, vnd_methods, has_animation, title)

        # Calculate the candidate's cost
        candidate_cost = calculate_cost(candidate_solution)

        # Check if the candidate's cost is the lowest
        if candidate_cost < min_cost:
            # Define the candidate solution as the current solution
            current_solution = candidate_solution
            min_cost = candidate_cost       # Define the candidate's cost as the lowest
            k = 0       # Reboot the count
        else:
            k += 1      # Add 1 if not improve

    return current_solution
