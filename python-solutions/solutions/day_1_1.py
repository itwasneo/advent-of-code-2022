def day_1_1() -> int:
    max = 0
    with open("../input/input_1_1.txt") as fp:
        current_elves_calories = 0
        while True:
            line = fp.readline()
            if not line:
                break
            if line == '\n' or len(line) == 0:
                if current_elves_calories > max:
                    max = current_elves_calories
                    current_elves_calories = 0
                else:
                    current_elves_calories = 0
            else:
                current_elves_calories += int(line)
    print("day_1_solution: %d" % max)
    return max
