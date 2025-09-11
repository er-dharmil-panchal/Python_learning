"""
📌 NumPy – Step 6 (Linear Algebra)

This file covers:
    - Dot Product & Matrix Multiplication
    - Transpose
    - Determinant
    - Inverse of a Matrix
    - Eigenvalues & Eigenvectors
    - Solving Linear Equations
    - Trace
    - Norms (Euclidean, Frobenius, ord=1, ord=inf)
    - Pseudo-inverse
    - Matrix Rank
    - Condition Number
    - More Eigenvalue Functions (eigh, eigvals)
    - Kronecker Product
    - Basic operations: sum, subtraction, min, max, argmin, argmax, mean, median, std, var, logical
    - Practice Tasks

📝 Summary:
    - NumPy linear algebra (numpy.linalg) allows matrix math, ML computations, physics, and data transformations.
    - Use np.dot() or @ for vector/matrix multiplication
    - Use np.linalg.det() for determinant
    - np.linalg.inv() for inverse
    - np.linalg.eig() / eigh() / eigvals() for eigenvalues & vectors
    - np.linalg.solve() to solve linear systems
    - Norms: np.linalg.norm() for vectors/matrices
    - Rank, pseudo-inverse, and condition number help check matrix properties and stability
"""

import numpy as np

# =============== Dot Product & Matrix Multiplication =================

# 👉🏻 Vector Dot Product

a = np.array([1, 2])
b = np.array([3, 4])

print(np.dot(a, b))  # 11
print(a @ b)  # 11

# 👉🏻 Matrix Multiplication
# Rule: (m×n) @ (n×p) = (m×p)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(np.dot(A, B))  # Dot product
print(A @ B)  # Matrix Multiplication

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[10, 11], [14, 15], [17, 18]])
print(np.dot(A, B))
print(A @ B)

# 3D arrays
# Both arrays must have 24 elements total
A = np.arange(24).reshape(2, 3, 4)  # shape (2,3,4)
B = np.arange(24).reshape(2, 4, 3)  # shape (2,4,3)

print("A shape:", A.shape)
print("B shape:", B.shape)

print("Dot product shape:", np.dot(A, B).shape)
print("@ shape:", (A @ B).shape)

# @ does clean matrix multiplication (works like in math).
# np.dot() does a generalized contraction → result has extra dimensions
"""
np.dot(A,B):
    Contracts last axis of A (4) with second-to-last of B (4).
    Remaining shape = (2,3) from A and (2,3) from B → (2,3,2,3)
    (that’s why extra dimensions appear).
A @ B:
    Treats first dimension (2) as batch size.
    Inside each batch, it does (3,4) @ (4,3) → (3,3).
    So result = (2,3,3).
"""

# =============== Transpose =================
A = np.array([[1, 2, 3], [4, 5, 6]])

print(A.T)
# [[1 4]
#  [2 5]
#  [3 6]]


# =============== Determinant =================
# Works only for square matrices (n×n).
# Determinant is useful to check:
#   If a matrix is invertible (det ≠ 0).
#   Properties in linear equations, transformations, eigenvalues etc.

# For a 2x2 matrix: det[[1,2],[3,4]] = 1*4 - 2*3 = -2
a = np.array([[1, 2], [3, 4]])
print(np.linalg.det(a))  # -2

# for a 3x3 matrix:
A = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
print(np.linalg.det(A))  # -306.0

# =============== Inverse of a Matrix =================
# Used in solving systems of equations.
A = np.array([[1, 2], [3, 4]])

inv_A = np.linalg.inv(A)
print(inv_A)

# Verify
print(A @ inv_A)  # Identity matrix
print(np.round(A @ inv_A))  # Now its clean 😉
# or
print(np.allclose(A @ inv_A, np.eye(2)))

# 3x3
A = np.array([[2, 1, 1], [1, 3, 2], [1, 0, 0]])

inv_A = np.linalg.inv(A)
print(inv_A)

# non invertible

A = np.array([[2, 4], [1, 2]])
print("Determinant:", np.linalg.det(A))  # 0

# Try inverse       :- error - LinAlgError: Singular matrix
# inv_A = np.linalg.inv(A)
# print(inv_A)

# =============== Eigenvalues & Eigenvectors =================
# ✔️ Very important in PCA, ML, physics, stability analysis.
A = np.array([[4, -2], [1, 1]])

values, vectors = np.linalg.eig(A)

print("Eigenvalues:", values)
print("Eigenvectors:\n", vectors)

# =============== Solving Linear Equations =================
# Gives exact solution without manually finding inverse.

# 2x + y = 11x + 3y = 13
# 2x + y = 13-------1
# 11x + 3y = 13-----2

# Convert to matrix - 2  1 | 13
#                     11 3 | 13
A = np.array([[2, 1], [11, 3]])  # Coefficient matrix
B = np.array([13, 13])  # Ans Matrix(Constants)
x, y = np.linalg.solve(A, B)
print(x, y)
print(np.linalg.solve(A, B))

# x + y = 7 -------1
# 2x - y = -1 -----2

A = np.array([[1, 1], [2, -1]])
B = np.array([7, -1])
print(np.linalg.solve(A, B))  # [2. 5.]

# =============== Some more functions =================

# 👉🏻 np.trace(A)
# Returns the sum of diagonal elements of a square matrix.
A = np.array([[1, 2], [3, 4]])
print(np.trace(A))  # Output: 5 (1 + 4)

# 👉🏻 np.linalg.norm(A)
# Computes the length or magnitude of a vector (or the "size" of a matrix in certain norms).
# Use cases: Measuring distance, normalizing vectors, error calculations in ML.
v = np.array([3, 4])
print(np.linalg.norm(v))  # Output: 5.0 (because sqrt(3^2 + 4^2) = 5)
print(np.linalg.norm(np.array([6, 8])))  # 10.0
# Length of vector      -> Distance, normalization

A = np.array([[1, 2], [3, 4]])
print(np.linalg.norm(A))  # Frobenius norm: sqrt(sum(A^2)) → 5.477
# Size of matrix        -> Matrix magnitude, error, ML loss

print(np.linalg.norm(A, ord=1))  # Max column sum → 6
print(np.linalg.norm(A, ord=np.inf))  # Max row sum → 7
print(np.linalg.norm(A, ord=2))  # Spectral norm → largest singular value

# 👉🏻 np.linalg.pinv(A)
# Computes the pseudo-inverse of a matrix.
# Some matrices aren’t square or aren’t invertible. Pseudo-inverse gives a "best possible" inverse.

A = np.array([[1, 2], [3, 4], [5, 6]])  # 3x2 matrix (non-square)
print(np.linalg.pinv(A))
# print(np.linalg.inv(A))         # numpy.linalg.LinAlgError: Last 2 dimensions of the array must be square


# 👉🏻 Matrix Rank -> np.linalg.matrix_rank(A)
# Check if a system of equations has a unique solution.
# Detect linear dependence.

A = np.array([[1, 2], [2, 4]])
print(np.linalg.matrix_rank(A))  # Output: 1 (second row is multiple of first)

B = np.array([[1, 2], [3, 4]])
print(np.linalg.matrix_rank(B))  # Output: 2 (full rank)

# 👉🏻 Condition Number -> np.linalg.cond(A)
# Measures how stable a matrix is for solving equations.
# Small errors in input → huge errors in output (unstable).
# Low value (~1): Stable.

A = np.array([[1, 2], [3, 4]])
print(np.linalg.cond(A))  # Output: ~14.93 (moderate)

B = np.array([[1, 2], [2.0001, 4]])
print(np.linalg.cond(B))  # Output: huge value → very unstable

# 👉🏻 More Eigenvalue Functions

# a) np.linalg.eigh(A)
# For symmetric or Hermitian matrices. More accurate & stable.
# Returns eigenvalues and eigenvectors.

A = np.array([[2, 1], [1, 2]])  # symmetric
vals, vecs = np.linalg.eigh(A)
print("Eigenvalues:", vals)
print("Eigenvectors:\n", vecs)

# b) np.linalg.eigvals(A)
# Returns only eigenvalues (faster if you don’t need vectors).

A = np.array([[4, -2], [1, 1]])
print(np.linalg.eigvals(A))  # Only eigenvalues

# 👉🏻 Kronecker Product
# Expands two matrices into a block matrix
# Useful: Advanced linear algebra, tensor operations, quantum computing.
A = np.array([[1, 2], [3, 4]])
B = np.array([[0, 5], [6, 7]])

print(np.kron(A, B))
# Output:
# [[ 0  5  0 10]
#  [ 6  7 12 14]
#  [ 0 15  0 20]
#  [18 21 24 28]]


# basic operations
A = np.array([[1, 2], [3, 4]])

# Sum
print(np.sum(A))  # 10
print(np.sum(A, axis=0))  # sum by column -> [4 6]
print(np.sum(A, axis=1))  # sum by row -> [3 7]

# Subtraction
B = np.array([[4, 3], [2, 1]])
print(A - B)  # element-wise subtraction -> [[-3 -1],[1 3]]

# Min & Max
print(np.min(A))  # 1
print(np.max(A))  # 4
print(np.min(A, axis=0))  # [1 2] min of each column
print(np.max(A, axis=1))  # [2 4] max of each row

# Index of min/max
print(np.argmin(A))  # 0 → index if flattened
print(np.argmax(A))  # 3 → index if flattened
print(np.argmin(A, axis=0))  # [0 0] min indices per column
print(np.argmax(A, axis=1))  # [1 1] max indices per row

print(np.mean(A))  # 2.5 overall mean
print(np.median(A))  # 2.5
print(np.std(A))  # standard deviation
print(np.var(A))  # variance

# Logical
print(np.all(A > 0))  # True if all elements > 0
print(np.any(A > 3))  # True if any element > 3

# =============== Practice Task =================

# 1. Compute dot product and @ multiplication for vectors [2,3,4] & [1,0,-1] and matrices [[1,2],[3,4]] & [[5,6],[7,8]].

v1 = np.array([2, 3, 4])
v2 = np.array([1, 0, -1])
print(np.dot(v1, v2))
print(v1 @ v2)

m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
print(np.dot(m1, m2))
print(m1 @ m2)

# 2. Find determinant and inverse of [[2,-1,0],[1,3,1],[0,2,1]].
A = np.array([[2, -1, 0], [1, 3, 1], [0, 2, 1]])
print(f"Determinant of A is {np.round(np.linalg.det(A))}")
inv_a = np.linalg.inv(A)
print(f"Inverse of A is \n{inv_a}")
print(f"Verification of A @ inv_A \n{np.round(A @ inv_a, 2)}")

# 3. Compute eigenvalues and eigenvectors of [[4,-2],[1,1]] and verify A @ v = λ*v.
m = np.array([[4, -2], [1, 1]])
value, vector = np.linalg.eig(m)
print("Eigenvalues:", value)
print("Eigenvectors:\n", vector)

# 4. Solve linear equations 3x+4y=10 and 2x-y=1 using np.linalg.solve().
m1 = np.array([[3, 4], [2, -1]])
m2 = np.array([10, 1])
print(np.linalg.solve(m1, m2))  # [1.27272727 1.54545455]

# 5. Compute Euclidean norm of [6,8,0], normalize it, and compute Frobenius, ord=1, ord=np.inf norms and trace of [[1,2],[3,4]].

v = np.array([6, 8, 0])
norm_v = np.linalg.norm(v)
print(norm_v)
# Normalize vector
v_normalized = v / norm_v
print("Normalized vector v:", v_normalized)  # Normalized vector v: [0.6 0.8 0. ]

# Matrix
A = np.array([[1, 2],
              [3, 4]])

# Frobenius norm (default)
fro_norm = np.linalg.norm(A)
print("Frobenius norm of A:", fro_norm)  # 5.477

# ord=1 norm (max column sum)
ord1_norm = np.linalg.norm(A, ord=1)
print("ord=1 norm of A:", ord1_norm)  # max(1+3,2+4) = 6

# ord=inf norm (max row sum)
ord_inf_norm = np.linalg.norm(A, ord=np.inf)
print("ord=inf norm of A:", ord_inf_norm)  # max(1+2,3+4) = 7

# Trace
trace_A = np.trace(A)
print("Trace of A:", trace_A)  # 1 + 4 = 5

# 6. Compute rank, condition number, and pseudo-inverse of [[1,2],[2,4]] and [[1,2],[3,4]].
A = np.array([[1, 2], [2, 4]])
B = np.array([[1, 2], [3, 4]])
print(f"Rank of A is {np.linalg.matrix_rank(A)}")
print(f"Rank of B is {np.linalg.matrix_rank(B)}")

print(f"Condition number of A is {np.linalg.cond(A)}")
print(f"Condition number of B is {np.linalg.cond(B)}")

print(f"Pseudo-inverse of A is \n{np.linalg.pinv(A)}")
print(f"Pseudo-inverse of V is \n{np.linalg.pinv(B)}")


"""
📌 Quick Recap
    - Dot Product & Matrix Multiplication → np.dot() or @
    - Transpose → .T
    - Determinant → np.linalg.det()
    - Inverse → np.linalg.inv()
    - Eigenvalues & Eigenvectors → np.linalg.eig(), eigh(), eigvals()
    - Solve linear systems → np.linalg.solve()
    - Trace → np.trace()
    - Norms → np.linalg.norm()
    - Pseudo-inverse → np.linalg.pinv()
    - Matrix Rank → np.linalg.matrix_rank()
    - Condition Number → np.linalg.cond()
    - Kronecker Product → np.kron()
    - Basic operations → sum, min, max, argmin, argmax, mean, median, std, var
    - Logical → np.all(), np.any()
"""