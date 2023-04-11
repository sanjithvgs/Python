def generateMatrix(A):
  array=[]
  for row_ind in range(A):
    temp=[]
    for col_ind in range(A):
      temp.append(0)
    array.append(temp)      
  x=0
  y=0
  value=1
  direction="right"
  boundary=0
  while value<=A*A:
    array[x][y]=value
    value+=1

    if direction=="right":
      y+=1
      if y==A-1-boundary:
        direction="down"

    elif direction=="down":
      x+=1
      if x==A-1-boundary:
        direction="left"

    elif direction=="left":
      y-=1
      if y==boundary:
        direction="top"

    elif direction=="top":
      x-=1
      if x==boundary+1:
        direction="right"
        boundary+=1

  return array

A=int(input("Enter a number to create spiral matix: "))
print(generateMatrix(A))


# output:
# Enter a number to create spiral matix: 5
# [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]