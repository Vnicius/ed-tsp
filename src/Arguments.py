# -*- coding: utf-8 -*-

import argparse


class Arguments():
    """Handle the arguments

    Attributes:
        args {Object} -- object with the arguments
    """

    def __init__(self):
        """Arguments constructor
        """

        parser = argparse.ArgumentParser()
        parser.add_argument(
            'instance', help="File with instances", type=str)
        parser.add_argument('-c', '--construction', help="Construction heuristic",
                            choices=['nearest', 'random'], default='random', type=str)
        parser.add_argument('-m', '--method', help="Heuristic method",
                            choices=['bi', 'fi', 'random', 'vnd', 'all'], default='all', type=str)
        parser.add_argument(
            '-l', '--limit', help="Limit for random and vnd methods", default=5, type=int)
        self.args = parser.parse_args()
