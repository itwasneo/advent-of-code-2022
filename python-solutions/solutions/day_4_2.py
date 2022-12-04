def day_4_2() -> int:
    result = 0
    with open("../input/input_4_1.txt") as fp:
        while True:
            line = fp.readline().strip()
            if not line:
                break
            groups = line.split(",")
            first = groups[0].split("-")
            second = groups[1].split("-")

            if int(first[0]) <= int(second[1]) and int(first[1]) >= int(second[0]):
                result += 1
    print("day_4_2_solution: %d" % result)
    return result
