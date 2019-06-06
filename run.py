# -*- coding: utf-8 -*-

from src.Arguments import Arguments
from src.InstanceReader import InstanceReader
from src.ConstructionHeuristic import ConstructionHeuristic
from src.utils.utils import calculate_cost, solution_to_string
from src.utils.plotsolution import plot_solution
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

        title = 'Best Improvement Method'
        best = best_improvement_method(
            initial_solution, has_animation=args.animate, title=title)
        print()
        print("BEST IMPROVEMENT METHOD: ", solution_to_string(best))
        print("BEST IMPROVEMENT METHOD COST: ",
              calculate_cost(best))

        if args.plot:
            plot_solution(best, title)

    if args.method in ['fi', 'all']:

        title = 'First Improvement Method'
        first = first_improvement_method(
            initial_solution, has_animation=args.animate, title=title)
        print()
        print("FIRST IMPROVEMENT METHOD: ", solution_to_string(first))
        print("FIRST IMPROVEMENT METHOD COST: ",
              calculate_cost(first))

        if args.plot:
            plot_solution(first, title)

    if args.method in ['random', 'all']:

        title = 'Random Method'
        random_solution = random_method(
            initial_solution, limit=args.limit, has_animation=args.animate, title=title)
        print()
        print("RANDOM METHOD: ", solution_to_string(random_solution))
        print("RANDOM METHOD COST: ", calculate_cost(
            random_solution))

        if args.plot:
            plot_solution(random_solution, title)

    if args.method in ['vnd', 'all']:

        title = 'VND Method'
        vnd_solution = vnd_method(
            initial_solution, samples=args.limit, has_animation=args.animate, title=title)
        print()
        print("VND METHOD: ", solution_to_string(vnd_solution))
        print("VND METHOD COST:", calculate_cost(vnd_solution))

        if args.plot:
            plot_solution(vnd_method, title)
