 A = [   [0, 0, 0, 0],
         [0, 0, 0, 1],
         [0, 0, 1, 1],
         [0, 1, 1, 1]    ]
n=len(A)
max_one=-float('inf')
result_index=0
for x in range(n):
    count=0
    for y in range(n):
        if A[x][y]==1:
            count+=1
    if count>max_one:
        max_one=count
        result_index=x
print(result_index)

# output:
# 3

# Row 3 contain maximum number of 1   [0, 1, 1, 1]