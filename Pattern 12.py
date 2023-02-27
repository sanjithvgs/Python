n=int(input("Enter a input n: "))
space=n
for i in range(1,n+1):
  print(" "*space,end="")
  for j in range(1,i+1):
    print(i,end=" ")
  space-=1
  print()

#   output:
# Enter a input n: 5
 #     1 
 #    2 2 
 #   3 3 3 
 #  4 4 4 4 
 # 5 5 5 5 5 
