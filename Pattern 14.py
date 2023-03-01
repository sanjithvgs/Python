n=int(input("Enter a input n: "))
for i in range(n,0,-1):
  for j in range(1,i+1):
    print(j,end=" ")
  print()

#   output:
# Enter a input n: 7
# 1 2 3 4 5 6 7 
# 1 2 3 4 5 6 
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 