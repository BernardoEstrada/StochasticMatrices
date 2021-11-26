import numpy as np
from fractions import Fraction
import helpers as h

def inputMatrix(rows: int):
    matrix = np.empty((rows, rows), dtype=Fraction)
    print("Enter the matrix row by row, separete the values with a space")
    for i in range(rows):
        row = list(map(Fraction, input().split()))
        matrix[i] = row
    return matrix

def isStochasticMatrix(matrix):
    for i in range(len(matrix)):
        if sum(matrix[i]) != 1:
            return False
    return True

def randomStochasticMatrix(n: int):
    matrix = np.random.rand(n, n)
    for i in range(len(matrix)):
        matrix[i] = matrix[i] / sum(matrix[i])
    return matrix

def matrixInit():
    choice = int(input("""1: Input Matrix\n2: Random Matrix\n3: Quit\nSelect a Value: """))
    if choice == 1:
        mat = inputMatrix(int(input("Enter the size of the matrix: ")))
        isStochastic = isStochasticMatrix(mat)
        if isStochastic:
            return (1 , mat)
        print("The matrix is not stochastic, please enter a stochastic matrix.")
        return (-1 , mat)
    elif choice == 2:
        return (2, randomStochasticMatrix(int(input("Enter the size of the matrix: "))))
    elif choice == 3:
        return (3, None)
    return (-1, -1)

def matrixInitUntilValid():
    res = -1
    while res == -1:
        try:
            (res, mat) = matrixInit()
            if res != -1: break
            h.printInvalidInput()
        except:
            h.printInvalidInput()
    return res, mat

if(__name__ == '__main__'):
    res, mat = matrixInitUntilValid()
    print(res)
    if res != 3:
        h.printMatrixWithRowSum(mat)
