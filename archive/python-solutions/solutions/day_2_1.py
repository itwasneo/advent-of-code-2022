SCORES = dict({
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
})


def day_2_1() -> int:
    total_score = 0
    with open("../input/input_2_1.txt") as fp:
        lines = fp.readlines()
        for line in lines:
            total_score += int(SCORES.get(line.strip()))

    print("day_2_1_solution: %d" % total_score)
    return total_score
