n=int(input("Enter a input n: "))
space=n-1
for i in range(1,n+1):
  print(" "*space+"*"*i,end="")
  space-=1
  print()

# output:
# Enter a input n: 7
#       *
#      **
#     ***
#    ****
#   *****
#  ******
# *******