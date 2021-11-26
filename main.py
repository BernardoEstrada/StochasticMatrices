import matrixInput as mi
import stateProbability as sp
import helpers as h

config = {
    "printDecimals": True,
    "printDigits": 6
}
mat = mi.randomStochasticMatrix(3)

while True:
    select = 0
    print("1: Change Matrix")
    print("2: Print Matrix")
    print("3: Get n steps")
    print("4: Get steady state")
    print("5: Check if matrix is regular")
    print("6: Change config")
    print("7: Quit")
    try:
        select = int(input("\nSelect an option: "))
    except:
        select = 0

    print("\n")
    if select == 1:
        res, mat = mi.matrixInitUntilValid()
        if res == 3:
            pass
    elif select == 2:
        h.printMatrixWithRowSum(mat, config["printDecimals"], config["printDigits"])
    elif select == 3:
        try:
            n = int(input("Enter the number of steps: "))
            sp.nSteps(mat, n)
        except:
            h.printInvalidInput()
    elif select == 4:
        print(sp.getSteadyState(mat))
    elif select == 5:
        try:
            limit = int(input("Enter attempt limit: "))
            print(sp.checkRegular(mat, limit))
        except:
            h.printInvalidInput()
    elif select == 6:
        try:
            config["printDecimals"] = input("Print as decimals (choosing no will print as fraction)? (y/n): ") == "y"
            config["printDigits"] = int(input("Print digits: "))
        except:
            h.printInvalidInput()
    elif select == 7:
        break
    else:
        h.printInvalidInput()

    print('―' * 100)
    print("\n")
    