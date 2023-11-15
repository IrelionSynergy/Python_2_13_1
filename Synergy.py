import random

def printMatrix(matrix):
    for i in matrix:
        print(*i)
    print()    

def randomNumber():
    return random.randint(-100, 100)

def sumMatrix(matrixOne, matrixTwo):
    matrixRezult = []
    for i in range(len(matrixOne)):
        lineOne = matrixOne[i]
        lineTwo = matrixTwo[i]
        lineRezult = []
        for j in range(len(lineOne)):
            lineRezult.append(lineOne[j] + lineTwo[j])
        matrixRezult.append(lineRezult)
    return matrixRezult

print('Задайте размер матрицы M x N')
m = int(input('M = '))
n = int(input('N = '))

matrixOne = [[randomNumber() for i in range(n)] for i in range(m)]
matrixTwo = [[randomNumber() for i in range(n)] for i in range(m)]

print('Матрица № 1')
printMatrix(matrixOne)
print('Матрица № 2')
printMatrix(matrixTwo)

print('Сумма матриц равна:')
printMatrix(sumMatrix(matrixOne, matrixTwo))