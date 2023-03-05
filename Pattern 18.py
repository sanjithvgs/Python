n=int(input("Enter a input n: "))
apla="aABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(n,0,-1):
  for j in range(1,i+1):
    print(apla[j],end=" ")
  print()

#   output:
# Enter a input n: 10
# A B C D E F G H I J 
# A B C D E F G H I 
# A B C D E F G H 
# A B C D E F G 
# A B C D E F 
# A B C D E 
# A B C D 
# A B C 
# A B 
# A 