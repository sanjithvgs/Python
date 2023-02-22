n=int(input("Enter a input n: "))
space=n-1
for i in range(n,0,-1):
  print(" "*space,end="")
  for j in range(1,n+1):
    if i<=j:
      print(j,end=" ")
  space-=1
  print()
  
# output:
# Enter a input n:7
#       7 
#      6 7 
#     5 6 7 
#    4 5 6 7 
#   3 4 5 6 7 
#  2 3 4 5 6 7 
# 1 2 3 4 5 6 7 