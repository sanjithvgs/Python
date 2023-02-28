n=int(input("Enter a input n: "))
apla="aABCDEFGHIJKLMNOPQRSTUVWXYZ"
space=n
for i in range(1,n+1):
  print(" "*space,end="")
  for j in range(1,i+1):
    print(apla[i],end=" ")
  space-=1
  print()

#   output:
# Enter a input n: 5
#     A 
#    B B 
#   C C C 
#  D D D D 
# E E E E E 
