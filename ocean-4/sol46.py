def sum_matrix(A,B):

    n = len(A)

    C = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):

            C[i][j] = A[i][j] + B[i][j]

    return C

A = [[1,2],[3,4]]
B = [[5,6],[7,8]]
print(sum_matrix(A,B))