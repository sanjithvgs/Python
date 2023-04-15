def solve(A, B):
    result_sub=[]
    for row in range(len(A)):
        temp=[]
        for col in range(len(A[0])):
            temp.append(A[row][col]-B[row][col])
        result_sub.append(temp)
    return result_sub

A =  [[1, 2, 3], 
      [4, 5, 6], 
      [7, 8, 9]]

B =  [[9, 8, 7], 
      [6, 5, 4], 
      [3, 2, 1]]

print("Subtraction of two matrix is: ",solve(A,B))

# output:
# Subtraction of two matrix is:  [[-8, -6, -4], [-2, 0, 2], [4, 6, 8]]