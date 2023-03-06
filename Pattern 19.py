n=int(input("Enter a input n: "))
a=1
space=n-1
for i in range(1,n+1):
  reach=False
  print("0 "*space,end="")
  for j in range(1,a+1):
    if i<a and not reach:
      print(i,end=" ")
      i+=1
    elif i==a:
      reach=True
      print(i,end=" ")
      i-=1
    elif i<a and reach:
      print(i,end=" ")
      i-=1
  print("0 "*space,end="")
  space-=1
  a+=2
  print()

#   output:
# Enter a input n: 4
# 0 0 0 1 0 0 0 
# 0 0 2 3 2 0 0 
# 0 3 4 5 4 3 0 
# 4 5 6 7 6 5 4 