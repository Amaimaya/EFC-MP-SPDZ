import time


def lu_decomposition(A):
    """
    Perform LU decomposition of a matrix A
    """
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]
    
    for j in range(n):
        L[j][j] = 1.0
        for i in range(j+1):
            s1 = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = A[i][j] - s1
        
        for i in range(j, n):
            s2 = sum(U[k][j] * L[i][k] for k in range(j))
            L[i][j] = (A[i][j] - s2) / U[j][j]

    return L, U

def forward_substitution(L, b):
    """
    Solve the system of linear equations Lx = b for x using forward substitution.
    """
    n = len(b)
    x = [0 for _ in range(n)]
    for i in range(n):
        x[i] = b[i] - sum(L[i][j] * x[j] for j in range(i))
    return x

def backward_substitution(U, y):
    """
    Solve the system of linear equations Ux = y for x using backward substitution.
    """
    n = len(y)
    x = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i+1, n))) / U[i][i]
    return x

def invert_matrix(A):
    n = len(A)
    L, U = lu_decomposition(A)
    # Initialize A_inv with dimensions [n][n], filled with 0s
    A_inv = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        e = [0]*n
        e[i] = 1  # ith column of the identity matrix
        y = forward_substitution(L, e)
        print(y)
        x = backward_substitution(U, y)
        # Assign the resulting x vector to the correct column in A_inv
        for j in range(n):
            A_inv[j][i] = x[j]

    # Manually transpose A_inv without using zip
    A_inv_transposed = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            A_inv_transposed[i][j] = A_inv[j][i]

    return A_inv_transposed


# Example matrix
A = [[0.2065972222222222, -0.15798611111111108, 0.059027777777777804, 0.0069444444444444475], [-0.15798611111111108, 0.2482638888888889, -0.04513888888888887, -0.03472222222222221], [0.059027777777777804, -0.04513888888888887, 0.24305555555555555, -0.06944444444444443], [0.0069444444444444475, -0.03472222222222221, -0.06944444444444443, 0.1388888888888889]]

# Invert the matrix using LU factorization
start = time.time()
A_inv = invert_matrix(A)
print(A_inv)
end = time.time()
print(end - start)
