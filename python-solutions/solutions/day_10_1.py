

def day_10_1() -> int:
    with open("../input/input_10_1.txt") as fp:
        lines = fp.readlines()
        cycle = 0
        register = 1
        score = 0
        for line in lines:
            tokens = line.split(" ")
            if len(tokens) == 1:
                cycle += 1
                score += get_cycle_score(cycle, register)
            else:
                cycle += 1
                score += get_cycle_score(cycle, register)
                cycle += 1
                register += int(tokens[1].strip())
                score += get_cycle_score(cycle, register)

    print(f"day_10_1_solution: {score}")

    return 60


def get_cycle_score(cycle: int, register: int) -> int:
    if (cycle + 1) == 20:
        return 20 * register
    elif (cycle + 1) == 60:
        return 60 * register
    elif (cycle + 1) == 100:
        return 100 * register
    elif (cycle + 1) == 140:
        return 140 * register
    elif (cycle + 1) == 180:
        return 180 * register
    elif (cycle + 1) == 220:
        return 220 * register
    else:
        return 0
