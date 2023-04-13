def solve(A, B):
    for row in range(len(A)):
        for col in range(len(A[0])):
            if A[row][col]!=B[row][col]:
                return False

    return True

A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
B = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(solve(A,B))

# output:
# True