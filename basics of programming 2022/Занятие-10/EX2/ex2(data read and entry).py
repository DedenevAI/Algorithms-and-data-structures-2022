'''code from Занятие-9/ex2.py'''
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


# matrix = [[-1,-2,-3],[-3,-4,-5],[-5,-6,-7]]
m = [x.strip().split() for x in open('C:\\Users\\Alex\\Desktop\\Основы\\DedenevAI\\basics of programming 2022\\Занятие-10\\EX2\\matrix_for_read.txt')]
print(m)



# matrixTrace = find_trace(matrix)
# print("След матрицы: ",matrixTrace)
# transform_matrix(matrix, matrixTrace)