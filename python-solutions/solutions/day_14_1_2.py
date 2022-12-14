from typing import Tuple


def day_14_1_2() -> Tuple[int, int]:

    # Utility function to read tile data
    sort_and_give_range = lambda *p: range(min(p), max(p)+1)

    # Set of locations that are blocked either by grid or sand
    blocked = set()

    # Reading data: putting grid data into the blocked set
    with open("../input/input_14.txt") as fp:
        for p in [[*map(eval, line.split("->"))] for line in fp.readlines()]:
            for (x1, y1), (x2, y2) in zip(p, p[1:]):
                blocked |= {(x, y) for x in sort_and_give_range(x1, x2)
                            for y in sort_and_give_range(y1, y2)}

    part_1_solution = 0

    # total grid tiles
    grid = len(blocked)

    # part_2 floor
    floor = max(p[1] for p in blocked)

    # This loop can calculate the results for both parts.
    # This loops continues until the sands raise up until the
    # sand sink.
    while (500, 0) not in blocked:

        # Sand sink location
        position = (500, 0)
        while True:

            # If sand gets lower than the max depth, part 1 gets solved
            if position[1] > floor:
                if not part_1_solution:
                    # Don't forget to subtract the actual grid tiles
                    part_1_solution = len(blocked) - grid
                break

            # Check whether the next position is available in given order
            # If you can't move continue with the next sand
            for dest in (position[0], position[1]+1), (position[0]-1, position[1]+1), (position[0]+1, position[1]+1), :
                if dest not in blocked:
                    position = dest
                    break
            else:
                break
        # Add the new rested sand to the blocked set
        blocked.add(position)

    print(f"day_14_1_solution: {part_1_solution}")
    print(f"day_14_2_solution: {len(blocked)- grid}")
    return (part_1_solution, len(blocked) - grid)
