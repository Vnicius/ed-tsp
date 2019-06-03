# -*- coding: utf-8 -*-
import math

class ConstructionHeuristic():
    def construct(self, instance):
        """Construct the inital solution
        
        Arguments:
            instance {Instance} -- instance object
        
        Returns:
            list -- initial solution
        """
        data_matrix = instance.data
        initial_solution = [0]

        while len(initial_solution) < instance.dimension:
            min_distance = math.inf
            min_distance_index = 0

            for index, distance in enumerate(data_matrix[initial_solution[-1]]):
                
                if (distance < min_distance) and (distance > 0.0) and (index not in initial_solution):
                    min_distance = distance
                    min_distance_index = index
            
            initial_solution.append(min_distance_index)
        
        return initial_solution
