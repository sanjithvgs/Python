n=int(input("Enter a input n: "))
space=int(n/2)
for i in range(1,n+1,2):
  print(" "*space,end="")
  for j in range(1,i+1):
    print("*",end="")
  space-=1
  print()

# output:
# Enter a input n: 10
#      *
#     ***
#    *****
#   *******
#  *********