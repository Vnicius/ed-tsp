# -*- coding: utf-8 -*-

from src.utils.Arguments import Arguments
from src.utils.InstanceReader import InstanceReader
from src.ConstructionHeuristic import ConstructionHeuristic
from src.utils.utils import calculate_cost, solution_to_string
from src.utils.plotsolution import plot_solution
from src.neighborhoodsearch import swap_method, two_opt_method, vnd_method

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

    if args.method in ['swap', 'all']:

        title = 'Best Improvement Method'
        best = swap_method(
            initial_solution, is_first=(args.improvement == 'first'), has_animation=args.animate, title=title)
        print()
        print("SWAP METHOD: ", solution_to_string(best))
        print("SWAP METHOD COST: ",
              calculate_cost(best))

        if args.plot:
            plot_solution(best, title)

    if args.method in ['2opt', 'all']:

        title = '2-OPT Method'
        two_opt_solution = two_opt_method(
            initial_solution, is_first=(args.improvement == 'first'), has_animation=args.animate, title=title)
        print()
        print("2-OPT METHOD: ", solution_to_string(two_opt_solution))
        print("2-OPT METHOD COST: ", calculate_cost(
            two_opt_solution))

        if args.plot:
            plot_solution(two_opt_solution, title)

    if args.method in ['vnd', 'all']:

        title = 'VND Method'
        vnd_solution = vnd_method(
            initial_solution, args.vnd_methods, has_animation=args.animate, title=title)
        print()
        print("VND METHOD: ", solution_to_string(vnd_solution))
        print("VND METHOD COST:", calculate_cost(vnd_solution))

        if args.plot:
            plot_solution(vnd_solution, title)
