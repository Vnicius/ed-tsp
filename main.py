# -*- coding: utf-8 -*-

from src.Arguments import Arguments
from src.InstanceReader import InstanceReader
from src.ConstructionHeuristic import ConstructionHeuristic

if __name__ == '__main__':
    args = Arguments().args
    reader = InstanceReader()
    instance = reader.get_instance(args.instance)
    initial_solution = ConstructionHeuristic().construct(instance)
