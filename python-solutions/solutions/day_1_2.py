from collections import deque

CAPACITY = 3


def day_1_2() -> int:
    top_3 = deque([], CAPACITY)
    current_elves_calories = 0

    with open("../input/input_1_1.txt") as fp:
        lines = fp.readlines()
        for line in lines:
            if line == '\n' or len(line) == 0:
                current_len = len(top_3)
                # queue is full
                if current_len == CAPACITY:
                    # bigger than 1st
                    # push front, pop back
                    if top_3[0] < current_elves_calories:
                        top_3.appendleft(current_elves_calories)
                        top_3.pop()
                    # pop back, push back
                    # bigger than 3rd
                    elif top_3[current_len-1] < current_elves_calories:
                        top_3.pop()
                        current_len = len(top_3)
                        # bigger than 2nd
                        if top_3[current_len-1] < current_elves_calories:
                            tmp = top_3.pop()
                            top_3.append(current_elves_calories)
                            top_3.append(tmp)
                        else:
                            top_3.append(current_elves_calories)
                elif current_len > 0 and current_len < CAPACITY:
                    # bigger than 1st
                    # push front
                    if top_3[0] < current_elves_calories:
                        top_3.appendleft(current_elves_calories)
                    # bigger than 2nd
                    elif top_3[current_len-1] < current_elves_calories:
                        tmp = top_3.pop()
                        top_3.append(current_elves_calories)
                        top_3.append(tmp)
                    # 3rd place is empty
                    else:
                        top_3.append(current_elves_calories)

                # queue is empty, just push front
                elif current_len == 0:
                    top_3.appendleft(current_elves_calories)
                else:
                    print("ERROR")
                current_elves_calories = 0
            else:
                current_elves_calories += int(line)

    print("day_1_2_solution: %d" % max)
    return sum(top_3)
