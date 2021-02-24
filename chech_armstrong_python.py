from math import *
def fun(num):
  res=0
  lst=list(num)
  l=len(lst)
  for i in range(0,l):
    a=pow( int(lst[i]),l)
    res=int(a)+res
  return res
  
num=input("Enter a number to check armstrong or not: ")
new=fun(num)
if (num ==str(new)):
  print("Armstrong number")
else:
  print("Not a Armstrong number")