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
n = int(input("Enter the order of the square matrix: "))
matrix = get_matrix_input(n)
print("The determinant of the matrix is:", determinant(matrix))