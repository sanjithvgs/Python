n=int(input("Enter a input n: "))
alpha="aABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(1,n+1):
  for j in range(1,i+1):
    print(alpha[j],end=" ")
  print()

# output:
# Enter a input n: 5
# A 
# A B 
# A B C 
# A B C D 
# A B C D E 