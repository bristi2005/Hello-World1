# Python program to add two matrices

# Define two matrices
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

# Initialize the result matrix with zeros
result = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]

# Perform matrix addition
for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]

# Display result
print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

print("\nSum of matrices A and B:")
for row in result:
    print(row)
