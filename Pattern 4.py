n=int(input("Enter a input n: "))
for i in range(1,n+1):
  for j in range(i):
    print(i,end=" ")
  print()

# output:
# Enter a input n: 6
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 
# 6 6 6 6 6 6 