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

    initial_solution = ConstructionHeuristic().construct_random(instance)
    print(initial_solution)
    print(calculate_cost(initial_solution, instance.data))

    best = best_improvement_method(initial_solution, instance.data)
    print("Best")
    print(best)
    print(calculate_cost(best, instance.data))

    #initial_solution = ConstructionHeuristic().construct_random(instance)
    # print(initial_solution)
    # print(calculate_cost(initial_solution, instance.data))
    first = first_improvement_method(initial_solution, instance.data)
    print("First")
    print(first)
    print(calculate_cost(first, instance.data))

    #initial_solution = ConstructionHeuristic().construct_random(instance)
    # print(initial_solution)
    # print(calculate_cost(initial_solution, instance.data))

    random_solution = random_method(initial_solution, instance.data)
    print("Random")
    print(random_solution)
    print(calculate_cost(random_solution, instance.data))

    vnd_solution = vnd_method(initial_solution, instance.data)
    print("VND")
    print(vnd_solution)
    print(calculate_cost(vnd_solution, instance.data))
