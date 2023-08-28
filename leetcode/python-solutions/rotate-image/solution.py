"""
solved in 25m
tests were already written and had solved once using backtoback video before
remember! on inner loop, start from layer!
"""

def rotate(matrix):
    layers = len(matrix) // 2
    size = len(matrix) - 1

    for layer in range(layers):
        for i in range(layer, size - layer):
            top = matrix[layer][i]
            right = matrix[i][size - layer]
            bottom = matrix[size - layer][size - i]
            left = matrix[size - i][layer]

            matrix[layer][i] = left
            matrix[i][size - layer] = top
            matrix[size - layer][size - i] = right
            matrix[size - i][layer] = bottom

    return matrix
