n=int(input("Enter a input n: "))
space=n-1
for i in range(1,n+1):
  print(" "*space,end="")
  for j in range(1,i+1):
    print(j,end=" ")
  space-=1
  print()

# output:
# Enter a input n: 10
#          1 
#         1 2 
#        1 2 3 
#       1 2 3 4 
#      1 2 3 4 5 
#     1 2 3 4 5 6 
#    1 2 3 4 5 6 7 
#   1 2 3 4 5 6 7 8 
#  1 2 3 4 5 6 7 8 9 
# 1 2 3 4 5 6 7 8 9 10 