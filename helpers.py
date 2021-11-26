
def bold(str: str) -> str:
    return f"\033[1m{str}\033[0m"

def printInvalidInput():
    print(bold("Invalid Input" + "\n"))

def printMatrixWithRowSum(matrix, dec=False, digits=0):
    for i in matrix:
        for j in i:
            if dec:
                if digits>=0:
                    print(round(j, digits), end=" ")
                else:
                    print(float(j), end=" ")
            else:
                print(j, end=" ")
        print("\t= ", sum(i))