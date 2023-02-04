def sum_col(A):
    row=len(A)
    col=len(A[0])
    res=[]
    for rows in range(row):
        add=0
        for cols in range(col):
            add+=A[cols][rows]
        res.append(add)
    return res

row,col=map(int,input("Enter row and column of 2D list: ").split())
A=[]
for i in range(row):
    row=[]
    for j in range(col):
        row.append(int(input(f"Enter element for row {i} and column {j}: ")))
    A.append(row)
print("Addition of column in 2D list: ",sum_col(A))
