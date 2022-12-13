import ast
from typing import List, Tuple


def recursive_compare(pair1, pair2) -> bool:
    if type(pair1) != type(pair2):
        if type(pair1) == int:
            pair1 = [pair1]
        elif type(pair2) == int:
            pair2 = [pair2]

    if type(pair1) == type(pair2) == int:
        if pair1 < pair2:
            return True
        elif pair1 > pair2:
            return False
    else:
        decision = None
        if len(pair1) < len(pair2):
            decision = True
        elif len(pair1) > len(pair2):
            decision = False

        for v1, v2 in zip(pair1, pair2):
            com = recursive_compare(v1, v2)
            if com is None:
                continue
            else:
                return com
        return decision


def day_13():
    with open("../input/input_13.txt") as fp:
        # parsing data with ast, pairing them as tuples
        # using ast.literal_eval to convert strings to python lists
        pairs = [(ast.literal_eval(y[0]), ast.literal_eval(y[1])) for y in [x.split("\n")
                                                                            for x in fp.read().split("\n\n")]]
        part_1 = 0
        for i, pair in enumerate(pairs):
            if recursive_compare(pair[0], pair[1]):
                part_1 += i+1

        part_2 = 1
        for d1 in [[[2]], [[6]]]:
            count_true = 0
            # increasing by 1 when the divider packets are bigger than other packets
            # this basically gives their indices in order list
            for pair in pairs:
                if recursive_compare(pair[0], d1):
                    count_true += 1
                if recursive_compare(pair[1], d1):
                    count_true += 1

            part_2 *= count_true + 1

        print(f"day_13_1_solution: {part_1}")
        print(f"day_13_2_solution: {part_2}")

        return (part_1, part_2)
