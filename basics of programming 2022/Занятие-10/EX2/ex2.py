''' old code '''
# @return trace(след) of matrix 
def find_trace (m):
        trace = []
        for row in range (0,len(m)):
            for term in range (0,len(m[row])):
                if term == row:
                    trace.append(m[row][term])
        return sum(trace)

# @this function transforms the original matrix according to the rule: divide even rows by the resulting value, leave odd rows unchanged
def transform_matrix (m, trace):
        for row in range (0,len(m)):
            string =''
            if row % 2 != 0:
                for term in range (0,len(m[row])):
                    string = string + str( round((m[row][term] / trace),2) ) + '    '
                print (string)
            else:
                for term in range (0,len(m[row])):
                    string = string + str(m[row][term]) + '    '
                print (string)
'''new code'''

#@return array with matrix
def open_file(f):
    array = []
    while True:
        x = f.readline().strip()
        if (x == ""):
            break
        array.append(str(x))
    return array

file_for_write1 = open("C:\\Users\\windows\\Desktop\\ex2w.txt", "w")

file_for_read = open("C:\\Users\\windows\\Desktop\\ex2.txt", "r")
matrix = open_file(file_for_read)
print("Начальная матрица:", matrix)


matrix = [[-1,-2,-3],[-3,-4,-5],[-5,-6,-7]]
matrixTrace = find_trace(matrix)
print("След матрицы: ",matrixTrace)
transform_matrix(matrix, matrixTrace)

 


