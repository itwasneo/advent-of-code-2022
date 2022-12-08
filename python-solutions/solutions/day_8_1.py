import numpy as np
import pprint
import sys

WIDTH = 99
HEIGHT = 99
np.set_printoptions(threshold=sys.maxsize)


def day_8_1(part_number: int) -> int:
    # Border trees
    result = 69
    with open("../input/input_8_1.txt") as fp:
        rows = []
        for i in range(HEIGHT):
            number_string = fp.readline()
            char_list = list(number_string)
            int_list = list(map(int, char_list[:-1]))
            int_list = int_list
            rows.append(int_list)

        num_array = np.array(rows)

        # To show visited trees
        zero_array = np.zeros((HEIGHT, WIDTH))

        # To show scenic scores
        scenic_scores = np.ones((HEIGHT, WIDTH, 4))

        # Calculate number of trees visible from left
        for i, row in enumerate(num_array):
            left_max = row[0]
            zero_array[i][0] = 1
            for j in range(WIDTH):
                if left_max < row[j]:
                    zero_array[i][j] = 1
                    left_max = row[j]

                # Add scenic score
                for k in range(1, j):
                    if row[j-k] < row[j]:
                        scenic_scores[i][j][0] += 1
                    else:
                        break

        # Calculate number of trees visible from right
        for i, row in enumerate(num_array):
            right_max = row[WIDTH-1]
            zero_array[i][WIDTH-1] = 1
            for j in range(WIDTH):
                if right_max < row[-j-1]:
                    zero_array[i][-j-1] = 1
                    right_max = row[-j-1]

                # Add scenic score
                for k in range(1, j):
                    if row[-j-1+k] < row[-j-1]:
                        scenic_scores[i][-j-1][1] += 1
                    else:
                        break

        # Calculate number of trees visible from top
        for i in range(WIDTH):
            col = num_array[:, i]
            top_max = col[0]
            zero_array[:][0] = 1
            for j in range(HEIGHT):
                if top_max < col[j]:
                    zero_array[j][i] = 1
                    top_max = col[j]

                # Add scenic score
                for k in range(1, j):
                    if col[j-k] < col[j]:
                        scenic_scores[j][i][2] += 1
                    else:
                        break

        # Calculate number of trees visible from bottom
        for i in range(WIDTH):
            col = num_array[:, i]
            bottom_max = col[HEIGHT-1]
            zero_array[:][HEIGHT-1] = 1
            for j in range(HEIGHT):
                if bottom_max < col[-j-1]:
                    zero_array[-j-1][i] = 1
                    bottom_max = col[-j-1]

                # Add scenic score
                for k in range(1, j):
                    if col[-j+k-1] < col[-j-1]:
                        scenic_scores[-j-1][i][3] += 1
                    else:
                        break

        printer = pprint.PrettyPrinter(
            indent=2, compact=False, width=30, depth=30)

        scores = []
        for row in scenic_scores:
            for j in row:
                scores.append(j[0] * j[1] * j[2] * j[3])
        part_1_solution = zero_array.sum()
        part_2_solution = max(scores)

        if part_number == 1:
            print(f"day_8_1_solution: {part_1_solution}")
            return part_1_solution
        elif part_number == 2:
            print(f"day_8_2_solution: {part_2_solution}")
            return part_2_solution
