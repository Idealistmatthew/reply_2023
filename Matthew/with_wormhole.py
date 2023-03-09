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


def outputfile(file, output_array):
    output = open(file, "w")
    for line in output_array:
        output.write(" ".join(str(x) for x in line))
        output.write("\n")


# __________________Parsing__________________________#


r = 3
c = 3
s = 3
largeNum = -10000
sample = np.array([[1, 2, 3], [22, -4, 40], [6, 40, -10]])


class Solution():
    def __init__(self, matrix, R, C, S, snake_list):
        self.matrix = matrix
        self.R = R
        self.C = C
        self.S = S
        self.snake_list = snake_list
        self.paths = []
        self.incident_list = []
        self.no_start_list = []

    def solve(self):
        for snake in self.snake_list:
            tmp = self.oneSnake(snake)
            self.paths.append(tmp)

    def findMax(self):
        max_index = np.argmax(self.matrix)
        max_row, max_col = np.unravel_index(max_index, self.matrix.shape)
        index = [max_row, max_col]
        max_value = self.matrix[index[0], index[1]]
        return max_value, index

    def getNeighbours(self, index0):
        row, col = index0[0], index0[1]
        up_index = [
            row-1, col] if row != 0 else [np.shape(self.matrix)[0]-1, col]
        down_index = [
            row+1, col] if row != np.shape(self.matrix)[0]-1 else [0, col]
        left_index = [row, col-1] if col != 0 else [row,
                                                    np.shape(self.matrix)[1]-1]
        right_index = [
            row, col+1] if col != np.shape(self.matrix)[1]-1 else [row, 0]
        indices = [up_index, down_index, left_index, right_index]

        up_value = self.matrix[up_index[0], up_index[1]]
        down_value = self.matrix[down_index[0], down_index[1]]
        left_value = self.matrix[left_index[0], left_index[1]]
        right_value = self.matrix[right_index[0], right_index[1]]
        values = [up_value, down_value, left_value, right_value]

        directions = ["U", "D", "L", "R"]
        max_value = max(values)
        direction = directions[values.index(max(values))]
        index = indices[values.index(max(values))]
        self.takenElement(index)

        return max_value, index, direction

    def takenElement(self, index0):
        row, col = index0[0], index0[1]
        self.matrix[row, col] = largeNum

    def oneSnake(self, s):
        direction_list = []
        max_val, index0 = self.findMax()
        points.append(max_val)
        coords = index0
        self.takenElement(index0)
        for i in range(s-1):
            val, index, direction = self.getNeighbours(index0)
            points.append(val)
            direction_list.append(direction)
            index0 = index
        output = coords[::-1] + direction_list
        return output


file = "01-chilling-cat.txt"
R, C, S, snake_list, sample = parse(file)
points = []
ops = []

SolveSnake = Solution(sample, R, C, S, snake_list)
SolveSnake.solve()
print(SolveSnake.paths)
# for s in snake_list:
#     op = oneSnake(s)
#     ops.append(op)

# points = np.array(points)
# print(sample, points)
# print(sum(points.astype(int)))
# print(ops)

outputfile("output-chilling-cat-1.txt", SolveSnake.paths)
