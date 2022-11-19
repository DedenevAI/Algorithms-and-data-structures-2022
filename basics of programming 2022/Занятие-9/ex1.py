# @returns the original matrix
def matrix(x):
    mat = []
    i = 0
    j = 0
    print("Fill the matrix with your numbers:")
    mat = [[0 for _ in range(x)] for _ in range(x)] # creating an array 
    for i in range(x):
        mat[i][i] = int(input()) # main diagonal
        for j in range(i + 1, x):
                mat[i][j] = int(input()) # upper triangle
                mat[j][i] = mat[i][j] # lower triangle

    for i in range(x): print(*mat[i])

n = int(input("Enter the size = "))
matrix(n)