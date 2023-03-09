import numpy as np
import parse

r = 3
c = 3 
s = 3
largeNum = -1000
sample = np.array([[1,2,3],[22,-4,40],[6,40,-10]])

def findMax(matrix):
    max_index = np.argmax(matrix)
    max_row, max_col = np.unravel_index(max_index, matrix.shape)
    index = [max_row, max_col]
    max_value = matrix[index[0], index[1]]
    return max_value, index

def getNeighbours(matrix, index0):
    row, col = index0[0], index0[1]
    up_index = [row-1, col] if row!=0 else [np.shape(matrix)[0]-1, col]
    down_index = [row+1, col] if row!=np.shape(matrix)[0]-1 else [0, col]
    left_index = [row, col-1] if col!=0 else [row, np.shape(matrix)[1]-1]
    right_index = [row, col+1] if col!=np.shape(matrix)[1]-1 else [row, 0]
    indices = [up_index, down_index, left_index, right_index]
    
    up_value = matrix[up_index[0], up_index[1]]
    down_value = matrix[down_index[0], down_index[1]]
    left_value = matrix[left_index[0], left_index[1]]
    right_value = matrix[right_index[0], right_index[1]]
    values = [up_value, down_value, left_value, right_value]

    directions = ["U", "D", "L", "R"]
    max_value = max(values)
    direction = directions[values.index(max(values))]
    index = indices[values.index(max(values))]
    takenElement(matrix, index)

    return max_value, index, direction

def takenElement(matrix, index0):
    row, col = index0[0], index0[1]
    matrix[row, col] = largeNum


def oneSnake(s):
    direction_list = []
    max_val, index0 = findMax(sample)
    points.append(max_val)
    coords = index0
    takenElement(sample, index0)
    for i in range(s-1):
        val, index, direction = getNeighbours(sample, index0)
        points.append(val)
        direction_list.append(direction)
        index0 = index
    output = coords + direction_list
    return output

file = "00-example.txt"
R, C, S, snake_list, sample = parse.parse(file)
points = []
ops = []

for s in snake_list:
    op = oneSnake(s)
    ops.append(op)

points = np.array(points)
print(sample, points)
print(sum(points.astype(int)))
print(ops)


