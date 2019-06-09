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
        parser.add_argument('-m', '--method', help="Heuristic approach",
                            choices=['swap', '2opt', 'vnd', 'all'], default='all', type=str)
        parser.add_argument('-i', '--improvement', help="Type of improvement choice",
                            choices=['best', 'first'], default='best', type=str)
        parser.add_argument('--vnd-methods', help="Sequence of the methods used in VND approach",
                            nargs='*', choices=['swap', 'swapbi', 'swapfi', '2opt', '2optbi', '2optfi'], default=['swap', '2opt'], type=str)
        parser.add_argument(
            '-p', '--plot', help='Plot the result', action='store_true')
        parser.add_argument('-a', '--animate',
                            help='Animated plot', action='store_true')
        self.args = parser.parse_args()
