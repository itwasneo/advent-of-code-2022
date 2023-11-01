import pprint
import sys
from typing import Tuple

printer = pprint.PrettyPrinter(width=sys.maxsize)

pixels = [[' '] * 40 for x in range(6)]


def day_10_2() -> str:
    with open("../input/input_10_1.txt") as fp:
        lines = fp.readlines()
        cycle = 0
        register = 1
        for line in lines:
            tokens = line.split(" ")
            if len(tokens) == 1:
                cycle += 1
                print_pixels(cycle, register)
            else:
                cycle += 1
                print_pixels(cycle, register)
                cycle += 1
                register += int(tokens[1].strip())
                print_pixels(cycle, register)

        print("day_10_2_solution: \n")
        for x in pixels:
            printer.pprint(''.join(x))

    return "str"


def print_pixels(cycle: int, register: int) -> Tuple[int, int]:
    rem = cycle
    if cycle >= 40:
        rem = cycle % 40
    if (register-1) <= rem and (register+1) >= rem:
        if cycle < 40:
            pixels[0][rem] = '#'
        elif cycle < 80:
            pixels[1][rem] = '#'
        elif cycle < 120:
            pixels[2][rem] = '#'
        elif cycle < 160:
            pixels[3][rem] = '#'
        elif cycle < 200:
            pixels[4][rem] = '#'
        elif cycle < 240:
            pixels[5][rem] = '#'
    # else:
        # print(f"rem: {rem} ------ register: {register}")
