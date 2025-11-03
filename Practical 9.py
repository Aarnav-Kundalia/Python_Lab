A_matrix = [[1, 2, 3, 4], [5, 6, 7, 8,]]
B_matrix = [[1, 2, 3], [4, 6, 8], [4, 9, 16], [6, 12, 18]]

if len(A_matrix[0]) != len(B_matrix):
    print("Columns of A must be equal to rows of B for multiplication.")
else:
    result = []
    for i in range(len(A_matrix)):
        row = []
        for j in range(len(B_matrix[0])):
            sum = 0
            for k in range(len(B_matrix)):
                sum += A_matrix[i][k] * B_matrix[k][j]
            row.append(sum)
        result.append(row)
    print("Resultant Matrix:")
    for row in result:
        print(row)


'''rows_A = int(input("Enter number of rows for Matrix A: "))
A_matrix = []
for i in range(rows_A):
    row = list(map(int, input(f"Enter the elements of {i+1} rows seperated by space").split()))
    A_matrix.append(row)
print("Matrix A:")
for row in A_matrix:
    print(row)'''

'''
rows = int(input("Enter number of rows for Matrix : "))
columns = int(input("Enter number of columns for Matrix : "))
matrix = []
for i in range(rows):
    for j in range(columns):
        element = (input(f"Enter the element at position ({i+1}, {j+1}): "))
        try:
            element = int(element)
        except ValueError:
            try:
                element = float(element)
            except ValueError:
                element = complex(element.replace(' ', ''))
        matrix.append(element)
print("Matrix:")
for i in range(rows):
    row = matrix[i*columns:(i+1)*columns]
    print(row)




def matrix_addition(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result

A_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B_matrix = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result = matrix_addition(A_matrix, B_matrix)
print("Resultant Matrix after Addition:")
for row in result:
    print(row)'''