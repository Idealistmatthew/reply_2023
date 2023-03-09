import numpy as np


# __________________Parsing__________________________#
def parse(file):
    input_0 = open(file, "r")
    input = input_0.readlines()
    mat_list = []
    matrix = np.array([])

    for i in range(len(input)):
        if i == 0:
            C, R, S = input[i].split()
        elif i == 1:
            snake_list = np.array([int(x) for x in input[i].split()])
        else:
            mat_list.append(
                [int(x) if x != "*" else x for x in input[i].split()])
    matrix = np.array(mat_list)
    return [C, R, S, snake_list, matrix]

# __________________Parsing__________________________#


def findMax(matrix):
    max_index = np.argmax(matrix)
    max_row, max_col = np.unravel_index(max_index, matrix.shape)
    max_value = matrix[max_row, max_col]
    return max_value, max_row, max_col


def getNeighbours(matrix, start_row, start_col):
    top_value = matrix[start_row-1, start_col]
    bottom_value = matrix[start_row+1, start_col]
    left_value = matrix[start_row, start_col-1]
    right_value = matrix[start_row, start_col+1]
    values = [top_value, bottom_value, left_value, right_value]
    max_value = max(values)
    index = values.index(max(values))
    return max_value, index


def outputfile(file, output_array):
    output = open(file, "w")
    for line in output_array:
        output.write(" ".join(str(x) for x in line))
        output.write("\n")


# def evaluate_strat(output_array, matrix, R, C):
#     score = 0
#     incidence_list = []
#     for snake in output_array:
#         row = snake[0]
#         col = snake[1]
#         score += matrix[start_row, start_col]
#         for move in snake[2:]:
#             if move == "U":
#                 row -= 1
#                 if row == -1:
#                     row  = R-1
#             elif move == "D":
#                 row += 1
#                 if row == R:
#                     row = 0
#             elif move == "L":
#                 start_col -= 1
#             elif move == "R":
#                 start_col += 1
#             else:
#                 pass
#             if matrix[start_row, start_col] == 0:
#                 score += 1
#             else:
#                 score -= 1
#                 incidence_list.append([start_row, start_col])
#     pass


if __name__ == "__main__":
    file = "00-example.txt"
    R, C, S, snake_list, matrix = parse(file)

    # _____Parsing Unit Tests_____#
    print("C: ", C)
    print("R: ", R)
    print("S: ", S)
    print("Snake List: ", snake_list)
    print("Matrix: ")
    print(matrix)
    print(type(snake_list))

    # _____Output Parsing Unit Tests_____#

    # test_output = [[0, 0, "R", "R", "D", 7, 2, "R", "R"],
    #                [6,1,"L", "U", "L", "D", "L", "U"],
    #                [1,1,"R", 3, 4, "R","R", "R" ],
    #                [7,1,"D", 3,4,"L"],
    #                [9,0,"U", "L"]]

    # test_output = [[2, 2, "U", "R", "D"],
    #                [3, 4, "D", "L", 2, 3, "D"],]
    # outputfile("output.txt", test_output)
