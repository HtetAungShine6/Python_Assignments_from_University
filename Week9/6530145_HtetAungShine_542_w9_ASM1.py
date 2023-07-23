def getSize(rows,columns):
    mat = []
    for i in range(rows):
        row = []
        for j in range(columns):
            userInput = int(input(f'Enter row#{i} column#{j} : '))
            row.append(userInput)
        mat.append(row)
    return mat

def matrixMultiplication(mat1, mat2):
    total = []
    for a in range(len(mat1)):
        row = []
        for b in range(len(mat2[0])):
            result = 0
            for c in range(len(mat2)):
                result += mat1[a][c] * mat2[c][b]
            row.append(result)
        total.append(row)
    return total

def matrixPrint(mat):
    for i in mat:
        for j in i:
            print(f'{j:3d}',end = '')
        print()

mat1row = int(input("Enter the size of rows for matrix 1 : "))
mat1col = int(input("Enter the size of columns for matrix 1 : "))
mat1 = getSize(mat1row,mat1col)

mat2row = int(input("Enter the size of rows for matrix 2 : "))
mat2col = int(input("Enter the size of columns for matrix 2 : "))
mat2 = getSize(mat2row,mat2col)

if mat1col != mat2row:
    print("The number of columns in the first matrixs should be equal to the number of rows in the second matrix!!!")
else:
    result = matrixMultiplication(mat1,mat2)
    print("RESULT : ")
    matrixPrint(result)