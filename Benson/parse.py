import numpy as np
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