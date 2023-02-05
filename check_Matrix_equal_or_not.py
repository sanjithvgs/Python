#To check both matrix are equal or not
def check_equal(A,B):
    row=len(A)
    col=len(A[0])
    res="Yes both are equal"
    for i in range(row):
        for j in range(col):
            if A[i][j]!=B[i][j]:
                res="No both are not equal"
                break
    return res

A=[[1, 2, 3],[4, 5, 6],[7, 8, 9]]
B=[[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(check_equal(A,B))

# A=[[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# B=[[1, 2, 3],[7, 8, 9],[4, 5, 6]]
# print(check_equal(A,B))
