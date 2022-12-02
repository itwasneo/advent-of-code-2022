SCORES = dict({
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
})


def day_2_2() -> int:
    total_score = 0
    with open("../input/input_2_1.txt") as fp:
        while True:
            line = fp.readline().strip()
            if not line:
                break
            total_score += int(SCORES.get(line))

    print("day_2_2_solution: %d" % total_score)
    return total_score
