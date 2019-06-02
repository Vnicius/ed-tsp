# -*- coding: utf-8 -*-

from src.Arguments import Arguments
from src.InstanceReader import InstanceReader

if __name__ == '__main__':
    args = Arguments().args
    reader = InstanceReader(args.instance)
    instance = reader.get_instance()
