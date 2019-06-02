# -*- coding: utf-8 -*-


class Instance():
    """Instance element

    Attributes:
        name {str} -- name of the instance
        dimension {int} -- dimension of the instance
        data {list} -- table with the data
    """

    def __init__(self, name, dimension, data):
        """Constructor

        Arguments:
            name {str} -- name of the instance
            dimension {int} -- dimension of the instance
            data {list} -- table with the data
        """
        self.name = name
        self.dimension = dimension
        self.data = data
