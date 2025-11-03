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

def matrix_transpose(matrix, rows, columns):
    transposed = []
    for j in range(columns):
        row = []
        for i in range(rows):
            row.append(matrix[i*columns + j])
        transposed.append(row)
    return transposed

transposed_matrix = matrix_transpose(matrix, rows, columns)
print("Transposed Matrix:")
for row in transposed_matrix:
    print(row)