def matrix_creation(n):
    if n <= 0:
        print("Number of Matrcies must be greater than 0")
        return {}
    matrices = {}
    for i in range(n):
        name = f"Matrix {i+1}"
        try:
            rows = int(input(f"Enter number of rows for {name}: "))
            columns = int(input(f"Enter number of columns for {name}: "))
        except Exception:
            print("Invalid input. Expected integers for rows and columns.")
            return {}
        if rows <= 0 or columns <= 0:
            print("Rows and columns must be greater than 0")
            return {}
        data = []
        for r in range(rows):
            row = []
            for c in range(columns):
                try:
                    element = int(input(f"Enter the element at position ({r+1}, {c+1}) for {name}: "))
                except Exception:
                    print("Invalid input. Expected an integer element.")
                    return {}
                row.append(element)
            data.append(row)
        matrices[name] = data
    print(matrices)    
    return matrices


def list_multiplication_possibilities(matrices):
    names = list(matrices.keys())
    possible = []
    for i in range(len(names)):
        for j in range(len(names)):
            if i == j:
                continue
            try:
                a = matrices[names[i]]
                b = matrices[names[j]]
                if not a or not b:
                    continue
                if len(a[0]) == len(b):
                    possible.append((names[i], names[j]))
            except Exception:
                continue
    if not possible:
        print("No matrix multiplication operations are possible among the given matrices.")
    else:
        print("Possible multiplications:")
        for i_name, j_name in possible:
            A = matrices[i_name]
            B = matrices[j_name]
            try:
                result_rows = len(A)
                result_cols = len(B[0])
            except Exception:
                result_rows = 0
                result_cols = 0
            print(f"- {i_name} x {j_name}: {i_name} = {A} , {j_name} = {B} => resultant dimensions {result_rows}x{result_cols}")
    return possible


def multiply_matrices(matrices, left_name, right_name):
    if left_name not in matrices or right_name not in matrices:
        print("One or both matrix names are invalid.")
        return None
    try:
        A = matrices[left_name]
        B = matrices[right_name]
        if not A or not B:
            print("The given input is not one of the possible operations.")
            return None
        a_cols = len(A[0])
        for row in A:
            if len(row) != a_cols:
                print("The given input is not one of the possible operations.")
                return None
        b_rows = len(B)
        b_cols = len(B[0])
        for row in B:
            if len(row) != b_cols:
                print("The given input is not one of the possible operations.")
                return None
        if a_cols != b_rows:
            print("The given input is not one of the possible operations.")
            return None
        result = []
        for r in range(len(A)):
            row = []
            for c in range(b_cols):
                total = 0
                for k in range(a_cols):
                    total += A[r][k] * B[k][c]
                row.append(total)
            result.append(row)
        print(f"Result of {left_name} x {right_name}:")
        for row in result:
            print(row)
        return result
    except Exception:
        print("The given input is not one of the possible operations.")
        return None


if __name__ == "__main__":
    num_matrices = int(input("Enter the number of matrices to create: "))
    matrices = matrix_creation(num_matrices)
    if not matrices:
        exit(0)
    list_multiplication_possibilities(matrices)
    left_name = input("Enter the left matrix name (e.g., Matrix 1), or press Enter to skip: ").strip()
    right_name = input("Enter the right matrix name (e.g., Matrix 2), or press Enter to skip: ").strip()
    if left_name and right_name:
        multiply_matrices(matrices, left_name, right_name)