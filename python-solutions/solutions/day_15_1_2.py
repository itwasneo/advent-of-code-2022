import sys
import numpy as np


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def combine_ranges(r1, r2):
    if r1[1] <= r2[0]:
        return (r1[0], r2[1])
    elif r1[0] >= r2[1]:
        return (r2[0], r1[1])
    else:
        return None


def merge(times):
    saved = list(times[0])
    for st, en in sorted([sorted(t) for t in times]):
        if st <= saved[1]:
            saved[1] = max(saved[1], en)
        else:
            yield tuple(saved)
            saved[0] = st
            saved[1] = en
    yield tuple(saved)


part_1_set = set()
with open("../../input/input_15.txt") as fp:
    sensors = []
    for p in fp.readlines():
        p1, p2 = p.split(":")
        a, b, c, d = p1.index("x=")+2, p1.index(","), p1.index("y=")+2, len(p1)
        e, f, g, h = p2.index("x=")+2, p2.index(","), p2.index("y=")+2, len(p2)
        x, y = int(p1[a:b]), int(p1[c:d])
        md = manhattan_distance(
            (x, y), (int(p2[e:f]), int(p2[g:h])))
        sensors.append(((x, y), md))
        if y + md > 2000000 and y - md < 2000000:
            y_dif = abs(y - 2000000)
            max_coverage = (md * 2 + 1)
            target_coverage = max_coverage - y_dif * 2
            half_target_coverage = int((target_coverage-1)/2)
            target_range = {x for x in range(
                x - half_target_coverage, x + half_target_coverage)}
            part_1_set |= target_range

    for i in range(4000000):
        coverage = []
        for sensor in sensors:
            if sensor[0][1] + sensor[1] >= i and sensor[0][1] - sensor[1] <= i:
                y_dif = abs(sensor[0][1] - i)
                max_coverage = (sensor[1] * 2 + 1)
                target_coverage = max_coverage - y_dif * 2
                half_target_coverage = int((target_coverage-1)/2)
                lower = 0 if sensor[0][0] - \
                    half_target_coverage < 0 else sensor[0][0]-half_target_coverage
                upper = 4000000 if sensor[0][0] + \
                    half_target_coverage > 4000000 else sensor[0][0]+half_target_coverage
                coverage.append((lower, upper))
        result = list(merge(sorted(coverage)))
        if len(result) > 1:
            print(4000000*(result[0][1]+1)+i)
            break
