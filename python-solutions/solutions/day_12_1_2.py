from typing import List, Tuple

data = [ln.strip() for ln in open("../input/input_12.txt")]
WIDTH = len(data[0])
HEIGHT = len(data)
for i, l in enumerate(data):
    for j, c in enumerate(l):
        if c == 'S':
            SOURCE = (i, j)
            data[i] = data[i].replace('S', 'a')
        if c == 'E':
            TARGET = (i, j)
            data[i] = data[i].replace('E', 'z')
HEIGHT_POINTS = [[ord(c)-ord('a') for c in w] for w in data]


def move(paths: List[Tuple[int, int]], visited: set) -> Tuple[List[Tuple[int, int]], bool]:
    nxt = []
    for r, c in paths:
        for p, q in [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]:
            tup = (p, q)
            if not (0 <= p < HEIGHT and 0 <= q < WIDTH) or HEIGHT_POINTS[p][q] > HEIGHT_POINTS[r][c]+1:
                continue
            if tup in visited:
                continue
            if tup == TARGET:
                return True, ()
            nxt.append(tup)
            visited.add(tup)
    return False, nxt


def solve(start: Tuple[int, int]) -> int:
    paths = [start]
    visited = set([start])
    for n in range(500):
        found, paths = move(paths, visited)
        if found:
            return n + 1
    return 500


def day_12_1():
    result = solve(SOURCE)
    print(f"day_12_1_solution: {result}")
    return result


def day_12_2():
    result = min(solve((i, j)) for i, l in enumerate(HEIGHT_POINTS)
                 for j, c in enumerate(l) if c == 0)
    print(f"day_12_2_solution: {result}")
    return result
