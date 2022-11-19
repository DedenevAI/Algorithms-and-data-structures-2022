'''code from Занятие-9/ex1.py'''
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
    return mat
'''new code'''
# @this function write matrix from previous function in the file
def write_matrix_in_file(m):
    with open("C:\\Users\\Alex\\Desktop\\Основы\\DedenevAI\\basics of programming 2022\\Занятие-10\\ex1.txt", "w") as f:
        for line in m:
            for elem in line:
                f.write(str(elem) + " ")
            f.write('\n')

n = int(input("Enter the size = "))
write_matrix_in_file(matrix(n))


