from fractions import Fraction
import numpy as np
import matrixInput as mi

# mat = mi.matrixInitUntilValid()
mat = np.array([
    [.65, .28, .07],
    [.15, .67, .18],
    [.12, .36, .52]
]).squeeze(),
print(mat)
print()

def nSteps(mat, n):
    for i in range(n):
        mat = np.matmul(mat, mat)
        mi.printMatrixWithRowSum(mat, True)
        print("\n")

def isRegular(mat):
    for i in mat:
        for j in i:
            if j <= 0:
                return False
    return True

def checkRegular(mat, limit: int):
    count = 0
    while not isRegular(mat):
        mat = np.matmul(mat, mat)
        count+=1
        if count > limit:
            return False
    return True

def getEqSystem(mat):
    mat = np.transpose(mat)
    for i in range(len(mat)):
        mat[i][i] = mat[i][i] - 1
    return mat

def getSteadyState(mat):
    mat = np.array(getEqSystem(mat).squeeze())
    print(type(mat), type(mat[0]), type(mat[0][0]))
    
    print(np.zeros(len(mat), dtype=Fraction))
    mat = np.linalg.solve(mat, np.zeros(len(mat)))
    return mat

mi.printMatrixWithRowSum(getSteadyState(mat), True, 5)
