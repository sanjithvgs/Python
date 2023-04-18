# Question:
# If A[i][j] = B then return (i * 1009 + j)
# If B is not present return -1.

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
B = 2

row=len(A)
col=len(A[0])
min_value=float('inf')
val=float('inf')
check_flag=False
for r in range(row):
    for c in range(col):
        if B==A[r][c]:
            row_val=r+1
            col_val=c+1
            val=row_val*1009+col_val
            check_flag=True
        min_value=min(val,min_value)
        
if check_flag:
    print(min_value)
else:
    print(-1)

# output:
# 1011


# A[1][2] = 2
# 1 * 1009 + 2 = 1011