# -*- coding: utf-8 -*-

from os import path
from time import time
import numpy as np
from src.utils.Arguments import Arguments
from src.utils.InstanceReader import InstanceReader
from src.ConstructionHeuristic import ConstructionHeuristic
from src.utils.utils import calculate_cost, solution_to_string
from src.utils.plotsolution import plot_solution
from src.neighborhoodsearch import swap_method, two_opt_method, vnd_method, vns_method, grasp_method


def best_gap(costs, best):
    gap_best = -1

    if best:
        gap_best = ((np.min(costs) - best)/best) * 100

    return gap_best


def main_table(args):
    reader = InstanceReader()
    instance = reader.get_instance(args.instance)
    construction = ConstructionHeuristic()
    initial_solution = []
    times = []
    costs = []
    instance_name = path.split(args.instance)[-1].split('.')[0]

    if args.method == 'all':
        for _ in range(10):

            if args.construction == 'nearest':
                t = time()
                initial_solution = construction.construct_nearest(instance)
            elif args.construction == 'random':
                t = time()
                initial_solution = construction.construct_random(instance)

            times.append(time() - t)
            costs.append(calculate_cost(initial_solution))
    else:
        if args.construction == 'nearest':
            initial_solution = construction.construct_nearest(instance)
        elif args.construction == 'random':
            initial_solution = construction.construct_random(instance)

    if args.method in ['swap', 'all']:

        title = 'Swap Improvement Method'

        for i in range(10):
            t = time()

            swap = swap_method(
                initial_solution, is_first=(args.improvement == 'first'), has_animation=args.animate, title=title)

            times.append(time() - t)
            costs.append(calculate_cost(swap))

    if args.method in ['2opt', 'all']:

        title = '2-OPT Method'

        for i in range(10):
            t = time()

            two_opt_solution = two_opt_method(
                initial_solution, is_first=(args.improvement == 'first'), has_animation=args.animate, title=title)

            times.append(time() - t)
            costs.append(calculate_cost(two_opt_solution))

    if args.method in ['vnd', 'all']:

        title = 'VND Method'

        for i in range(10):
            t = time()

            vnd_solution = vnd_method(
                initial_solution, args.vnd_methods, has_animation=args.animate, title=title)

            times.append(time() - t)
            costs.append(calculate_cost(vnd_solution))

    if args.method in ['vns', 'all']:

        title = 'VNS Method'

        for i in range(10):
            t = time()

            vns_solution = vns_method(
                initial_solution, args.vnd_methods, interations=args.number_interations, has_animation=args.animate, title=title)

            times.append(time() - t)
            costs.append(calculate_cost(vns_solution))

    if args.method in ['grasp', 'all']:

        title = 'GRASP Method'

        for i in range(10):
            t = time()

            grasp_solution = grasp_method(
                initial_solution, args.vnd_methods, instance, interations=args.number_interations, has_animation=args.animate, title=title)

            times.append(time() - t)
            costs.append(calculate_cost(grasp_solution))

    print(
        f'{instance_name}, {args.optimal}, {np.around(np.mean(costs), 5)}, {np.min(costs)}, {np.around(np.mean(times), decimals=5)}, {np.around(best_gap(costs, args.optimal), 5)}')


def main(args):
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
        swap = swap_method(
            initial_solution, is_first=(args.improvement == 'first'), has_animation=args.animate, title=title)
        print()
        print("SWAP METHOD: ", solution_to_string(swap))
        print("SWAP METHOD COST: ",
              calculate_cost(swap))

        if args.plot:
            plot_solution(swap, title)

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

    if args.method in ['vns', 'all']:

        title = 'VNS Method'
        vns_solution = vns_method(
            initial_solution, args.vnd_methods, interations=args.number_interations, has_animation=args.animate, title=title)
        print()
        print("VNS METHOD: ", solution_to_string(vns_solution))
        print("VNS METHOD COST:", calculate_cost(vns_solution))

        if args.plot:
            plot_solution(vns_solution, title)

    if args.method in ['grasp', 'all']:

        title = 'GRASP Method'
        grasp_solution = grasp_method(
            initial_solution, args.vnd_methods, instance, interations=args.number_interations, has_animation=args.animate, title=title)
        print()
        print("GRASP METHOD: ", solution_to_string(grasp_solution))
        print("GRASP METHOD COST:", calculate_cost(grasp_solution))

        if args.plot:
            plot_solution(grasp_solution, title)


if __name__ == '__main__':
    args = Arguments().args
    # main(args)
    main_table(args)
