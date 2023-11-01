def manhattan_distance(p1, p2):
    """
    Calculates the Manhattan distance between given 2 points
    """
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def merge(times):
    """
    Merges given time intervals
    """
    saved = list(times[0])
    for st, en in sorted(times):
        if st <= saved[1]:
            saved[1] = max(saved[1], en)
        else:
            yield tuple(saved)
            saved[0] = st
            saved[1] = en
    yield tuple(saved)


with open("../../input/input_15.txt") as fp:
    sensors = []
    part_1_coverage_ranges = []
    for p in fp.readlines():
        p1, p2 = p.split(":")
        a, b, c, d = p1.index("x=")+2, p1.index(","), p1.index("y=")+2, len(p1)
        e, f, g, h = p2.index("x=")+2, p2.index(","), p2.index("y=")+2, len(p2)
        x, y = int(p1[a:b]), int(p1[c:d])
        md = manhattan_distance(
            (x, y), (int(p2[e:f]), int(p2[g:h])))
        sensors.append(((x, y), md))

    #     if y + md > 2000000 and y - md < 2000000:
    #         y_dif = abs(y - 2000000)
    #         max_coverage = (md * 2 + 1)
    #         target_coverage = max_coverage - y_dif * 2
    #         half_target_coverage = int((target_coverage-1)/2)
    #         part_1_coverage_ranges.append(
    #             (x - half_target_coverage, x + half_target_coverage))
    # part_1_total_coverage = merge(sorted(part_1_coverage_ranges))
    # part_1_solution = 0
    # while True:
    #     try:
    #         s, e = next(part_1_total_coverage)
    #         part_1_solution += e - s
    #     except StopIteration:
    #         break
    # print(f"day_15_1_solution: {part_1_solution}")

    for i in range(4000000):
        coverage = []
        for sensor in sensors:
            if sensor[0][1] + sensor[1] >= i and sensor[0][1] - sensor[1] <= i:
                y_dif = abs(sensor[0][1] - i)
                lower = 0 if (l := sensor[0][0] - sensor[1] + y_dif) < 0 else l
                upper = 4000000 if (
                    u := sensor[0][0] + sensor[1] - y_dif) > 4000000 else u
                coverage.append((lower, upper))
        result = list(merge(sorted(coverage)))
        if len(result) > 1:
            print(4000000*(result[0][1]+1)+i)
            break
