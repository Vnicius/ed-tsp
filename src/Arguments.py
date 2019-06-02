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
            'instance', help="Arquivo com as instâncias", type=str)
        self.args = parser.parse_args()
