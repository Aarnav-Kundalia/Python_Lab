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


'''rows_B = int(input("Enter number of rows for Matrix B: "))
columns_B = int(input("Enter number of columns for Matrix B: "))
B_matrix = []
for i in range(rows_B):
    for j in range(columns_B):
        element = int(input(f"Enter the element at position ({i+1}, {j+1}): "))
        B_matrix.append(element)
print("Matrix B:")
for i in range(rows_B):
    row = B_matrix[i*columns_B:(i+1)*columns_B]
    print(row)'''

'''
'''