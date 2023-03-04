n=int(input("Enter a input n: "))
x=1
for i in range(1,n+1):
  for j in range(i):
    print(x,end=" ")
    x+=1
  print()

#   output:
# Enter a input n: 6
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 
# 16 17 18 19 20 21 