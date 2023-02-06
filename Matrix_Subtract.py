#Matrix Subraction
A =  [[1, 2, 3], 
      [4, 5, 6], 
      [7, 8, 9]]

B =  [[9, 8, 7], 
      [6, 5, 4], 
      [3, 2, 1]]

row=len(A)
col=len(A[0])
res=[]
for r in range(row):
  temp=[]
  for c in range(col):
    a=A[r][c]-B[r][c]
    temp.append(a)
  res.append(temp)
print(res)  #[[-8, -6, -4], [-2, 0, 2], [4, 6, 8]]