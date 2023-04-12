def solve(A, B):
    for row in range(len(A)):
        for col in range(len(A[0])):
            A[row][col]=A[row][col]*B
    return A

A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
B = 2 
print(solve(A,B))

# output:
# [[2, 4, 6], [8, 10, 12], [14, 16, 18]]