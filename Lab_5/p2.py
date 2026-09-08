A =  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

sum_of_elements = sum(x for row in A for x in row)

print(sum_of_elements)

n = len(A)

diagonal = [A[i][i] for i in range(n)]
print(diagonal)

anti_diagonal = [A[i][n-i-1] for i in range(n)]
print(anti_diagonal)

# m0 m1 m2
# m3 m4 m5
# m6 m7 m8

# imp->
def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return sum((-1) ** j * matrix[0][j] * determinant([row[:j] + row[j+1:] for row in matrix[1:]]) for j in range(len(matrix)))

print(determinant(A))