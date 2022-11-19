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


matrix = [[-1,-2,-3],[-3,-4,-5],[-5,-6,-7]]
matrixTrace = find_trace(matrix)
print("След матрицы: ",matrixTrace)
transform_matrix(matrix, matrixTrace)