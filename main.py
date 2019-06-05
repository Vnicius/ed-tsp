# -*- coding: utf-8 -*-

from src.Arguments import Arguments
from src.InstanceReader import InstanceReader
from src.ConstructionHeuristic import ConstructionHeuristic
from src.utils.utils import calculate_cost, solution_to_string
from src.neighborhoodsearch import best_improvement_method, first_improvement_method, random_method, vnd_method

if __name__ == '__main__':
    args = Arguments().args
    reader = InstanceReader()
    instance = reader.get_instance(args.instance)
    construction = ConstructionHeuristic()
    initial_solution = []

    if args.construction == 'nearest':
        initial_solution = construction.construct_nearest(instance)
    elif args.construction == 'random':
        initial_solution = construction.construct_random(instance)

    print("INITIAL: ", solution_to_string(initial_solution))
    print("INITIAL COST: ", calculate_cost(initial_solution))

    if args.method in ['bi', 'all']:
        best = best_improvement_method(initial_solution)
        print()
        print("BEST IMPROVEMENT METHOD: ", solution_to_string(best))
        print("BEST IMPROVEMENT METHOD COST: ",
              calculate_cost(best))

    if args.method in ['fi', 'all']:
        first = first_improvement_method(initial_solution)
        print()
        print("FIRST IMPROVEMENT METHOD: ", solution_to_string(first))
        print("FIRST IMPROVEMENT METHOD COST: ",
              calculate_cost(first))

    if args.method in ['random', 'all']:

        random_solution = random_method(
            initial_solution, args.limit)
        print()
        print("RANDOM METHOD: ", solution_to_string(random_solution))
        print("RANDOM METHOD COST: ", calculate_cost(
            random_solution))

    if args.method in ['vnd', 'all']:

        vnd_solution = vnd_method(initial_solution, args.limit)
        print()
        print("VND METHOD: ", solution_to_string(vnd_solution))
        print("VND METHOD COST:", calculate_cost(vnd_solution))
