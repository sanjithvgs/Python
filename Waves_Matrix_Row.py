N=int(input()) 
mat=[]
for _ in range(N):
  a=list(map(int,input().split()))
  mat.append(a)
r=len(mat)
c=len(mat[0])
for col in range(c):
  if col%2==0:
    for row in range(r):
      print(mat[row][col],end=" ")
  else:
    for row in range(r-1,-1,-1):
      print(mat[row][col],end=" ")

#Input:
# 3
# 4 1 2
# 7 4 4
# 3 7 4

# Output:
# 4 7 3 7 4 1 2 4 4 