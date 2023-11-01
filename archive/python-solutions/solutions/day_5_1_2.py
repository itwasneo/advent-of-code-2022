def day_5_1_2(problem_number: int) -> str:

    def is_empty(token: str):
        return token == "[*]"

    stack = [[], [], [], [], [], [], [], [], []]

    with open("../input/input_5_1.txt") as fp:
        # Filling crates into each pile
        for i in range(8):
            line = fp.readline()
            crates = line.split(" ")
            for j in range(9):
                if not is_empty(crates[j]):
                    if j is not 8:
                        stack[j].append(crates[j].replace(
                            "[", "").replace("]", ""))
                    else:
                        stack[j].append(crates[j].replace(
                            "[", "").replace("]", "").replace("\n", ""))

        # Reading redundant lines
        tmp = fp.readline()
        tmp = fp.readline()

        for i in range(9):
            stack[i].reverse()
        while True:
            line = fp.readline()
            if not line:
                break
            tokens = line.split()

            # Problem 2 solution differs here
            if problem_number == 2:
                to_move = []
                for i in range(int(tokens[1])):
                    to_move.append(stack[int(tokens[3]) - 1].pop())

                # Don't forget to  reverse it
                to_move.reverse()
                stack[int(tokens[5]) - 1] = stack[int(tokens[5]) - 1] + to_move

            # Problem 1 solution
            else:
                for i in range(int(tokens[1])):
                    # pop and push
                    stack[int(tokens[5]) -
                          1].append(stack[int(tokens[3]) - 1].pop())

    result = "".join([x[-1] for x in stack])
    print("day_5_%d_solution: %s" % (problem_number, result))
    return result
