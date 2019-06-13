# -*- coding: utf-8 -*-
import math
import random


class ConstructionHeuristic():
    def construct_nearest(self, instance, inital=0):
        """Construct the inital solution

        Arguments:
            instance {Instance} -- instance object

        Returns:
            list -- initial solution
        """
        data_graph = instance.data
        initial_solution = [data_graph[inital]]

        while len(initial_solution) < instance.dimension:
            last_node = initial_solution[-1]
            nearest_nodes = sorted(last_node.neighborhood,
                                   key=(lambda x: x.cost))
            nearest_neighbor = None

            for neighbor in nearest_nodes[1:]:
                if neighbor.node.key not in [node.key for node in initial_solution]:
                    initial_solution.append(neighbor.node)
                    break

        return initial_solution

    def construct_random(self, instance):
        initial_solution = random.sample(instance.data, len(instance.data))

        return initial_solution
