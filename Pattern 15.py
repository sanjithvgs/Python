n=int(input("Enter a input n: "))
for i in range(1,n+1):
  for j in range(n,0,-1):
    if i<=j:
      print(j,end=" ")
  print()

#   output:
# Enter a input n: 10
# 8 7 6 5 4 3 2 1 
# 8 7 6 5 4 3 2 
# 8 7 6 5 4 3 
# 8 7 6 5 4 
# 8 7 6 5 
# 8 7 6 
# 8 7 
# 8 