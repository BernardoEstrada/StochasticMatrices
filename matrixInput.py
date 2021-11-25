import numpy as np
from fractions import Fraction

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

def printMatrixWithRowSum(matrix, dec=False, digits=0):
    for i in matrix:
        for j in i:
            if dec:
                print(float(j), end=" ")
            elif digits!=0:    
                print(round(j, dec), end=" ")
            else:
                print(j, end=" ")
        print("\t= ", sum(i))

def matrixInit():
    choice = int(input("""1: Input Matrix\n2: Random Matrix\nSelect a Value: """))
    if choice == 1:
        mat = inputMatrix(int(input("Enter the size of the matrix: ")))
        isStochastic = isStochasticMatrix(mat)
        if isStochastic:
            return (1 , mat)
        print("The matrix is not stochastic, please enter a stochastic matrix.")
        return (-1 , mat)
    elif choice == 2:
        return (2, randomStochasticMatrix(int(input("Enter the size of the matrix: "))))
    return (-1, -1)

def matrixInitUntilValid():
    res = -1
    while res == -1:
        (res, mat) = matrixInit()
        if res != -1: break
        print("Invalid Input\n")
    return mat

if(__name__ == '__main__'):
    printMatrixWithRowSum(matrixInitUntilValid())
