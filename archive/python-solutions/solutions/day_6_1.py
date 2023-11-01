from collections import deque


def day_6_1() -> int:
    queue = deque(maxlen=14)
    result = 69
    cnt = 0
    with open("../input/input_6_1.txt") as fp:
        while True:

            c = fp.read(1)
            if not c:
                break
            cnt += 1
            queue.append(c)
            if len(queue) > 13:
                if len(queue) == len(set(queue)):
                    break

    print("day_6_1_solution: %d" % cnt)
    return result
