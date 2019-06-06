# -*- coding: utf-8 -*-
import math
import matplotlib.pyplot as plt
from copy import copy
import random


def get_plot_values(graph, has_points=False):
    xs = []
    ys = []
    xs_line = []
    ys_line = []
    N = len(graph)

    if has_points:
        for node in graph:
            xs.append(node.point.x)
            ys.append(node.point.y)

        xs_line, ys_line = xs, ys

    else:
        for i in range(N):
            xs.append(150.0 + 100 * math.cos(math.pi * 2 * i / N))
            ys.append(150.0 + 100 * math.sin(math.pi * 2 * i / N))

        for node in graph:
            xs_line.append(xs[node.key])
            ys_line.append(ys[node.key])

    xs_line.append(xs_line[0])
    ys_line.append(ys_line[0])

    return xs, ys, xs_line, ys_line


def plot_solution(graph, title="", has_points=False, show_key=False):
    xs, ys, xs_line, ys_line = get_plot_values(graph, has_points=has_points)

    plt.title(title)
    plt.plot(xs_line, ys_line, 'r')
    plt.plot(xs, ys, 'bo')
    plt.plot([xs_line[0]], [ys_line[0]], 'ro')

    if show_key:
        for index, (x, y) in enumerate(zip(xs, ys)):
            plt.text(x, y, str(index), color="green", fontsize=12)

    plt.show()


def plot_animated(graph, title="", has_points=False, show_key=False):
    xs, ys, xs_line, ys_line = get_plot_values(graph, has_points=has_points)

    plt.clf()
    plt.title(title)
    plt.plot(xs_line, ys_line, 'r')
    plt.plot(xs, ys, 'bo')
    plt.plot([xs_line[0]], [ys_line[0]], 'ro')

    if show_key:
        for index, (x, y) in enumerate(zip(xs, ys)):
            plt.text(x, y, str(index), color="green", fontsize=12)

    plt.pause(0.05)
