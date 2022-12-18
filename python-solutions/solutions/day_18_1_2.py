with open("../../input/input_18.txt") as fp:
    cubes = set([(int(x), int(y), int(z.strip()))
                 for x, y, z in [l.split(",") for l in fp.readlines()]])
    # max_x = max([x for x, _, _ in cubes])
    # max_y = max([y for _, y, _ in cubes])
    # max_z = max([z for _, _, z in cubes])
    # min_x = min([x for x, _, _ in cubes])
    # min_y = min([y for _, y, _ in cubes])
    # min_z = min([z for _, _, z in cubes])

    ta = 0
    for c in cubes:
        for o in cubes.difference(c):
            if c[0] == o[0] and c[1] == o[1] and abs(c[2] - o[2]) == 1:
                ta += 1
            elif c[0] == o[0] and c[2] == o[2] and abs(c[1] - o[1]) == 1:
                ta += 1
            elif c[1] == o[1] and c[2] == o[2] and abs(c[0] - o[0]) == 1:
                ta += 1

    print(f"day_18_1_solution: {len(cubes) * 6 - ta}")
