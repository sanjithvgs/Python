n=int(input("Enter a input n: "))
alpha="aABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(1,n+1):
  for j in range(1,i+1):
    print(alpha[i],end=" ")
  print()

# output:
# Enter a input n: 7
# A 
# B B 
# C C C 
# D D D D 
# E E E E E 
# F F F F F F 
# G G G G G G G 