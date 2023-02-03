def Transpose(A):
    res=[]
    for col_val in range(len(A[0])):
        temp=[]
        for row_val in range(len(A)):
            tep=A[row_val][col_val]
            temp.append(tep)
        res.append(temp)
    return res


row,col=map(int,input("Enter row and column of 2D list: ").split())
A=[]
for i in range(row):
    row=[]
    for j in range(col):
        row.append(int(input(f"Enter element for row {i} and column {j}: ")))
    A.append(row)
print("The Transpose for given matrix is :",Transpose(A))

# A=[[1,4,7],
#    [2,5,8],
#    [3,6,9]]
#
# o/p:
# [[1,2,3],
# [4,5,6]
# [7,8,9]]
