import numpy as np

def matrix_addition(A, B):
    return np.add(A, B)

def matrix_subtraction(A, B):
    return np.subtract(A, B)

def matrix_multiplication(A, B):
    return np.dot(A, B)

def matrix_transpose(A):
    return np.transpose(A)

def matrix_inverse(A):
    return np.linalg.inv(A)

def matrix_determinant(A):
    return np.linalg.det(A)

def eigenvalues_eigenvectors(A):
    eigenvals, eigenvecs = np.linalg.eig(A)
    return eigenvals, eigenvecs

def svd_decomposition(A):
    U, S, V = np.linalg.svd(A)
    return U, S, V

def startmatrix():
    A_rows = int(input("Enter the number of rows for matrix A: "))
    A_cols = int(input("Enter the number of columns for matrix A: "))
    A_elements = []

    print("Enter the elements of matrix A (row-wise): ")
    for _ in range(A_rows):
        row = []
        for _ in range(A_cols):
            element = float(input())
            row.append(element)
        A_elements.append(row)

    A = np.array(A_elements)

    B_rows = int(input("Enter the number of rows for matrix B: "))
    B_cols = int(input("Enter the number of columns for matrix B: "))
    B_elements = []

    print("Enter the elements of matrix B (row-wise): ")
    for _ in range(B_rows):
        row = []
        for _ in range(B_cols):
            element = float(input())
            row.append(element)
        B_elements.append(row)

    B = np.array(B_elements)

    print("Matrix Calculator Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Inverse (for matrix A)")
    print("6. Determinant (for matrix A)")
    print("7. Eigenvalues and Eigenvectors (for matrix A)")
    print("8. Singular Value Decomposition (SVD) (for matrix A)")

    choice = int(input("Enter your choice (1-8): "))

    if choice == 1:
        result = matrix_addition(A, B)
        print("Result:")
        print(result)
    elif choice == 2:
        result = matrix_subtraction(A, B)
        print("Result:")
        print(result)
    elif choice == 3:
        result = matrix_multiplication(A, B)
        print("Result:")
        print(result)
    elif choice == 4:
        result = matrix_transpose(A)
        print("Result:")
        print(result)
    elif choice == 5:
        result = matrix_inverse(A)
        print("Result:")
        print(result)
    elif choice == 6:
        result = matrix_determinant(A)
        print("Result:")
        print(result)
    elif choice == 7:
        eigenvals, eigenvecs = eigenvalues_eigenvectors(A)
        print("Eigenvalues:")
        print(eigenvals)
        print("Eigenvectors:")
        print(eigenvecs)
    elif choice == 8:
        U, S, V = svd_decomposition(A)
        print("U:")
        print(U)
        print("S:")
        print(S)
        print("V:")
        print(V)
    else:
        print("Invalid choice. Please select a number from 1 to 8.")
