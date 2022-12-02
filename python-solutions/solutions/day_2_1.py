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
        while True:
            line = fp.readline().strip()
            if not line:
                break
            total_score += int(SCORES.get(line))

    print("day_2_1_solution: %d" % total_score)
    return total_score
