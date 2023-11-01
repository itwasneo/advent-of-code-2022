import numpy as np
import re
from enum import Enum
import functools


class Status(Enum):
    OPEN = 0
    CLOSE = 1
    PENDING = 2


class Valve:
    __slots__ = ('rate', 'leads')


graph = dict()


@functools.cache
def dfs(opened, node, time_left):  # function for dfs
    if time_left <= 0:
        return 0
    best = 0
    for neighbour in graph[node].leads:
        best = max(best, dfs(opened, neighbour, time_left-1))

    if node not in opened and graph[node].rate > 0 and time_left > 0:
        opened = set(opened)
        opened.add(node)
        new_sum = (time_left-1) * graph[node].rate
        for neighbour in graph[node].leads:
            best = max(
                best,
                new_sum +
                dfs(frozenset(opened), neighbour, time_left-2)
            )

    return best


with open("../../input/input_16.txt") as fp:
    lines = fp.readlines()
    for i, line in enumerate(lines):
        p1, p2 = [x.strip() for x in line.split(";")]
        tokens_1 = p1.split(" ")

        new_valve = Valve()
        new_valve.rate = int(tokens_1[4].split("=")[1])
        pattern = r"\b(?:valve|valves)\b"
        regex = re.compile(pattern)
        new_valve.leads = [x.strip() for x in regex.split(p2)[1].split(",")]
        graph[tokens_1[1]] = new_valve

    # Driver Code
    print(f"day_16_1_solution: {dfs(frozenset(), 'AA', 30)}")
