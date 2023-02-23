n=int(input("Enter a input n: "))
space=n
apla="aABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(1,n+1):
  print(" "*space,end="")
  for j in range(1,i+1):
    print(apla[j],end=" ")
  space-=1
  print()

# output:
# Enter a input n: 6
#       A 
#      A B 
#     A B C 
#    A B C D 
#   A B C D E 
#  A B C D E F