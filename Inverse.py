def get_matrix_input(n):
    matrix = []
    for i in range(n):
        row = list(map(float, input(f"Enter the elements of row {i+1} separated by space: ").split()))
        if len(row) != n:
            raise ValueError(f"Row {i+1} must have exactly {n} elements.")
        matrix.append(row)
    return matrix
def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for c in range(n):
        minor = [row[:c] + row[c+1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * determinant(minor)
    return det
def get_cofactor(matrix, p, q):
    return [row[:q] + row[q+1:] for i, row in enumerate(matrix) if i != p]
def adjoint(matrix):
    n = len(matrix)
    adj = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            sign = (-1) ** (i + j)
            cofactor = get_cofactor(matrix, i, j)
            adj[j][i] = sign * determinant(cofactor)
    return adj
def inverse(matrix):
    det = determinant(matrix)
    if det == 0:
        raise ValueError("Matrix is singular and cannot be inverted.")
    adj = adjoint(matrix)
    n = len(matrix)
    inv = [[adj[i][j] / det for j in range(n)] for i in range(n)]
    return inv
n = int(input("Enter the order of the square matrix: "))
matrix = get_matrix_input(n)
inv_matrix = inverse(matrix)
print("The inverse of the matrix is:")
for row in inv_matrix:
    print(row)