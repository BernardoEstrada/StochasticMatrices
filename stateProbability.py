from fractions import Fraction
import numpy as np
import matrixInput as mi
import helpers as h

def nSteps(mat, n):
    for i in range(n):
        mat = np.matmul(mat, mat)
        h.printMatrixWithRowSum(mat, True, 4)
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
            return "Is regular"
    return "Is not regular"

def getEqSystem(mat):
    mat = np.transpose(mat)
    for i in range(len(mat)):
        mat[i][i] = mat[i][i] - 1
    mat = np.vstack([mat, [1]*len(mat)])
    mat = np.array(mat).astype(np.float64)
    b = np.array([0]*len(mat))
    b[len(mat)-1] =  1

    return (mat, b)

def getSteadyState(mat):
    (mat, b) = getEqSystem(mat)

    return np.linalg.lstsq(mat,b, rcond=None)[0]


if __name__ == "__main__":
    res, mat = mi.matrixInitUntilValid()
    if res == 3:
        exit()
    print(getSteadyState(mat))