def diagonal_sum(A):
    sum=0
    for row_v in range(len(A)):
        for col_v in range(len(A[0])):
            if row_v==col_v:
                sum+=A[row_v][col_v]
    return sum

row,col=map(int,input("Enter row and column of 2D list: ").split())
A=[]
for i in range(row):
    row=[]
    for j in range(col):
        row.append(int(input(f"Enter element for row {i} and column {j}: ")))
    A.append(row)
print("The sum of all diagonal in matrix is: ",diagonal_sum(A))

#A=[[1,2,3],
 # [4,5,6],
 # [7,8,9]]

# 1+5+9
 #o/p: 15
