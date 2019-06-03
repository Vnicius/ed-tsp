# -*- coding: utf-8 -*-
import numpy as np
from src.Instance import Instance


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
            data = np.zeros(shape=(dimension, dimension))

            file.readline()

            for i in range(dimension):
                line = file.readline()
                numbers = []

                for item in line.split(' '):
                    try:
                        number = int(item)
                        numbers.append(number)
                    except ValueError:
                        pass
                data[i] = numbers

        return Instance(name, dimension, data)
