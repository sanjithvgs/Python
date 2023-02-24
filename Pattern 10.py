n=int(input("Enter a input n: "))
space=n
apla="aABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(n,0,-1):
  print(" "*space,end="")
  for j in range(1,n+1):
    if i<=j:
      print(apla[j],end=" ")
  space-=1    
  print()

# output:
# Enter a input n: 5
#      E 
#     D E 
#    C D E 
#   B C D E 
#  A B C D E 