from typing import Tuple, List
from enum import Enum
import math


def traverse_2(head: Tuple[int, int], tail: Tuple[int, int]) -> Tuple[int, int]:
    x_difference = head[0] - tail[0]
    y_difference = head[1] - tail[1]
    distance = abs(head[0] - tail[0]) + \
        abs(head[1] - tail[1])
    if distance >= 2:
        if abs(x_difference) > abs(y_difference):
            return (head[0]-int(math.copysign(1, x_difference)), head[1])
        elif abs(x_difference) < abs(y_difference):
            return (head[0], head[1]-int(math.copysign(1, y_difference)))
        else:
            return tail
    else:
        return tail


def day_9_1() -> int:
    result = 0
    with open("../input/input_9.txt") as fp:
        body = [(0, 0), (0, 0)]
        tail_positions = set()
        tail_positions.add(body[1])
        lines = fp.readlines()
        for line in lines:
            tokens = line.split(" ")
            for i in range(int(tokens[1][:-1])):
                if tokens[0] == 'R':
                    body[0] = (body[0][0] + 1, body[0][1])
                elif tokens[0] == 'L':
                    body[0] = (body[0][0] - 1, body[0][1])
                elif tokens[0] == 'U':
                    body[0] = (body[0][0], body[0][1] + 1)
                elif tokens[0] == 'D':
                    body[0] = (body[0][0], body[0][1] - 1)
                else:
                    raise("Unknown behavior")
                body[1] = traverse_2(body[0], body[1])
                tail_positions.add(body[1])
        result = len(tail_positions)
    print(f"day_9_1_solution: {result}")
    return result


def traverse_body(node: Tuple[int, int], nxt: Tuple[int, int]) -> Tuple[Tuple[int, int], bool]:
    x_difference = node[0] - nxt[0]
    y_difference = node[1] - nxt[1]
    distance = abs(x_difference) + abs(y_difference)
    if distance >= 2:
        if abs(x_difference) > abs(y_difference):
            return((node[0] - int(math.copysign(1, x_difference)), node[1]), True)
        elif abs(x_difference) < abs(y_difference):
            return((node[0], node[1] - int(math.copysign(1, y_difference))), True)
        else:
            return((node[0] - int(math.copysign(1, x_difference)), node[1] - int(math.copysign(1, y_difference))), True)
    else:
        return (nxt, False)


def day_9_2() -> int:
    result = 0
    with open("../input/input_9.txt") as fp:
        body = [(0, 0) for i in range(10)]
        tail_positions = set()
        tail_positions.add(body[9])
        lines = fp.readlines()
        for line in lines:
            tokens = line.split(" ")
            direction = tokens[0]
            for i in range(int(tokens[1][:-1])):
                if tokens[0] == 'R':
                    body[0] = (body[0][0] + 1, body[0][1])
                elif tokens[0] == 'L':
                    body[0] = (body[0][0] - 1, body[0][1])
                elif tokens[0] == 'U':
                    body[0] = (body[0][0], body[0][1] + 1)
                elif tokens[0] == 'D':
                    body[0] = (body[0][0], body[0][1] - 1)
                else:
                    raise("Unknown behavior")
                keep_going = False
                for i in range(9):
                    body[i+1], keep_going = traverse_body(body[i], body[i+1])
                    if not keep_going:
                        break
                # small tweak to not to add 9th tail when
                # it doesn't change
                if keep_going:
                    tail_positions.add(body[9])
        result = len(tail_positions)
        print(f"day_9_2_solution: {result}")
    return result
