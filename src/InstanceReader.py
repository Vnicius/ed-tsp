# -*- coding: utf-8 -*-
import numpy as np
from src.Instance import Instance
from src.Node import Node
from src.Neighbor import Neighbor


class InstanceReader():
    """Read the file of instances
    """

    def get_instance(self, instance_path):
        instance = None
        name = ""
        dimension = ""
        data = []

        with open(instance_path, 'r', encoding='utf-8') as file:
            name = file.readline().split(' ')[-1]
            dimension = int(file.readline().split(' ')[-1])
            data = []

            file_type = file.readline().strip()

            if file_type == 'EDGE_WEIGHT_SECTION':
                data = self.__get_instance_teste(file, dimension)
            elif file_type == 'DISPLAY_DATA_SECTION':
                data = self.__get_instance_tsp_cup(file, dimension)

        return Instance(name, dimension, data)

    def __get_instance_teste(self, file, dimension):
        data = np.zeros(shape=(dimension, dimension))

        for i in range(dimension):
            line = file.readline()
            numbers = []

            for item in line.split(' '):
                try:
                    number = float(item)
                    numbers.append(number)
                except ValueError:
                    pass
            data[i] = numbers

        return self.__convert_to_graph(data, dimension)

    def __get_instance_tsp_cup(self, file, dimension):
        data_points = np.zeros(shape=(dimension, 2))
        data = np.zeros(shape=(dimension, dimension))

        for i in range(dimension):
            line = file.readline()

            numbers_count = 0
            for item in line.split():
                try:
                    number = float(item)
                    if numbers_count >= 1:
                        data_points[i][numbers_count - 1] = number

                    numbers_count += 1
                except ValueError:
                    pass

        for index, point in enumerate(data_points):
            for neighbor_index in range(dimension):
                neighbor = data_points[neighbor_index]

                data[index][neighbor_index] = np.sqrt(
                    (point[0] - neighbor[0])**2.0 + (point[1] - neighbor[1])**2.0).round()

        return self.__convert_to_graph(data, dimension)

    def __convert_to_graph(self, data, dimension):
        nodes = [Node(i) for i in range(dimension)]

        for i, costs in enumerate(data):
            neighborhood = []

            for j, cost in enumerate(costs):
                if cost != 0.0:
                    neighborhood.append(Neighbor(node=nodes[j], cost=cost))

            nodes[i].neighborhood = neighborhood

        return nodes
