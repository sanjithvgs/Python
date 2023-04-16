A = [ [1, 2],
      [3, 4] ]
n=len(A)
result_sum=0
for x in range(n):
    for y in range(n):
        result_sum+=A[x][y]*(x+1)*(y+1)*(n-x)*(n-y)
    
print(result_sum)

# The submatrices are [1], [2], [3], [4], [1, 2], [3, 4], [1, 3], [2, 4] and [[1, 2], [3, 4]].
# Total sum = 40