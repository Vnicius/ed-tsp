# -*- coding: utf-8 -*-

from src.Arguments import Arguments
from src.InstanceReader import InstanceReader
from src.ConstructionHeuristic import ConstructionHeuristic
from src.utils.utils import calculate_cost
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

    print("INITIAL: ", initial_solution)
    print("INITIAL COST: ", calculate_cost(initial_solution, instance.data))
    print()

    if args.method == 'bi':
        best = best_improvement_method(initial_solution, instance.data)
        print("BEST IMPROVEMENT METHOD: ", best)
        print("BEST IMPROVEMENT METHOD COST: ",
              calculate_cost(best, instance.data))

    elif args.method == 'fi':
        first = first_improvement_method(initial_solution, instance.data)
        print("FIRST IMPROVEMENT METHOD: ", first)
        print("FIRST IMPROVEMENT METHOD COST: ",
              calculate_cost(first, instance.data))

    elif args.method == 'random':

        random_solution = random_method(
            initial_solution, instance.data, args.limit)
        print("RANDOM METHOD: ", random_solution)
        print("RANDOM METHOD COST: ", calculate_cost(
            random_solution, instance.data))

    elif args.method == 'vnd':

        vnd_solution = vnd_method(initial_solution, instance.data, args.limit)
        print("VND METHOD: ", vnd_solution)
        print("VND METHOD COST:", calculate_cost(vnd_solution, instance.data))

    elif args.method == 'all':
        best = best_improvement_method(initial_solution, instance.data)
        print("BEST IMPROVEMENT METHOD: ", best)
        print("BEST IMPROVEMENT METHOD COST: ",
              calculate_cost(best, instance.data))
        print()

        first = first_improvement_method(initial_solution, instance.data)
        print("FIRST IMPROVEMENT METHOD: ", first)
        print("FIRST IMPROVEMENT METHOD COST: ",
              calculate_cost(first, instance.data))
        print()

        random_solution = random_method(
            initial_solution, instance.data, args.limit)
        print("RANDOM METHOD: ", random_solution)
        print("RANDOM METHOD COST: ", calculate_cost(
            random_solution, instance.data))
        print()

        vnd_solution = vnd_method(initial_solution, instance.data, args.limit)
        print("VND METHOD: ", vnd_solution)
        print("VND METHOD COST:", calculate_cost(vnd_solution, instance.data))
    else:
        print("Chose a valid method!")
