import numpy as np
from numpy.random.mtrand import exponential
import matrixInput as mi

mat = mi.matrixInitUntilValid()
print()

def nSteps(mat, n):
    for i in range(n):
        mat = np.dot(mat, mat)
        mi.printMatrixWithRowSum(mat, False, 4)
        print("\n")

nSteps(mat, 10)