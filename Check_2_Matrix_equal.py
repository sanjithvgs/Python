#To check given 2 matrix are equal or not
def same(A,B):
    row=len(A)
    col=len(A[0])
    res="Yes Equal"
    for i in range(row):
        for j in range(col):
            if A[i][j]!=B[i][j]:
                res="Not Equal"
                break
    return res

#Equal
A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[1,2,3],[4,5,6],[7,8,9]]
print(same(A,B))  

#Not Equal
A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[1,2,3],[7,8,9],[10,11,12]]
print(same(A,B))