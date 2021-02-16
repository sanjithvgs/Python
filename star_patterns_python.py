n=int(input("Enter the count"))
for i in range (0,n):
  for j in range (0,i+1):
    print("*",end='')
  print(" ")
for i in range (n):
  for j in range (1,n):
    print("*",end='')
  n-=1
  print(" ")