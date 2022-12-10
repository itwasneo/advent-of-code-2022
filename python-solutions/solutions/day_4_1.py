def day_4_1() -> int:
    result = 0
    with open("../input/input_4_1.txt") as fp:
        lines = fp.readlines()
        for line in lines:
            groups = line.split(",")
            first = groups[0].split("-")
            second = groups[1].split("-")

            if int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1]) or int(second[0]) >= int(first[0]) and int(second[1]) <= int(first[1]):
                result += 1
    print("day_4_1_solution: %d" % result)
    return result
