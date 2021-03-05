''' Get Binary value from user , 
print Addition and Multiplication of binary value in Integer '''

from math import *
# First binary value convertion
a=input("Enter a binary value: ")
lst=[]
lst=a
z=0
lst2=[]
num=len(lst)

for i in range(1,num+1):
  bi=int(pow(2,i-1))
  lst2.append(bi)
lst2.reverse()
for i in range(len(lst2)):
  if lst[i]== '1':
    z=z+lst2[i]
print(a,"-->",z)

# second binary value convertion 
a=input("Enter another binary value: ")
lst=[]
lst=a
y=0
lst2=[]
num=len(lst)

for i in range(1,num+1):
  bi=int(pow(2,i-1))
  lst2.append(bi)
lst2.reverse()
for i in range(len(lst2)):
  if lst[i]== '1':
    y=y+lst2[i]
print(a,"-->",y)
print("The Addition of two binary value is :",z+y)
print("The Multiplication of two binary value is :",z*y)

