def solve(A, B):
    result_sum=[]
    for row in range(len(A)):
        temp=[]
        for col in range(len(A[0])):
            temp.append(A[row][col]+B[row][col])
        result_sum.append(temp)
    return result_sum

A = [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]]

B = [[9, 8, 7], 
     [6, 5, 4], 
     [3, 2, 1]]

print("Sum of two matrix is: ",solve(A,B))

# output:
# Sum of two matrix is:  [[10, 10, 10], [10, 10, 10], [10, 10, 10]]